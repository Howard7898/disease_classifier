#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Binary Relevance Multi-Label Disease Classifier
================================================

Unified script for training Binary Relevance classifiers for occupational health screening.

Author: Teh-Hao Teng, Tae-Rim Lee, Seung Hyeok Byeon, Mun-Taek Choi
Institution: Sungkyunkwan University
Date: 2024

Usage:
    # Paper setting (no oversampling, Table 4 algorithm per disease)
    python train_classifier.py --disease all --output results/
    # Extension: oversampling inside each CV training fold
    python train_classifier.py --disease all --output results/ --oversample
    # Optional: compare LR/SVM/RF/GB per disease by CV F1
    python train_classifier.py --disease all --output results/ --select-algorithm
"""

import argparse
import os
import warnings
from pathlib import Path
from typing import Dict, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import RandomOverSampler
from imblearn.pipeline import Pipeline as ImbPipeline
from sklearn.metrics import (
    confusion_matrix,
    precision_recall_fscore_support,
    roc_curve,
    auc,
    classification_report
)
from sklearn.exceptions import UndefinedMetricWarning

# Suppress warnings
warnings.filterwarnings("ignore", category=UndefinedMetricWarning)
warnings.filterwarnings("ignore", category=FutureWarning)


class DiseaseClassifier:
    """Binary classifier for a single disease using Binary Relevance approach."""
    
    # Table 3 (paper): hyperparameter search range per algorithm
    ALGORITHM_PARAM_GRIDS = {
        'lr': {
            'C': [0.01, 0.1, 1],
            'solver': ['newton-cg', 'lbfgs', 'liblinear']
        },
        'svm': {
            'C': [0.1, 1, 10],
            'kernel': ['poly', 'rbf', 'sigmoid'],
            'gamma': ['scale', 'auto']
        },
        'rf': {
            'n_estimators': [100, 150, 200],
            'min_samples_leaf': [1, 2, 3]
        },
        'gb': {
            'learning_rate': [0.001, 0.01, 0.1],
            'min_samples_split': [2, 3, 4],
            'n_estimators': [50, 100, 150]
        }
    }

    # Table 4 (paper): best algorithm per disease
    DISEASE_ALGORITHM = {
        'obesity': 'rf',
        'liver': 'gb',
        'highpressure': 'gb',
        'diabete': 'gb',
        'kidney': 'gb',
        'dyslipidemia': 'gb',
        'circul': 'lr',
        'musculoskeletal': 'gb',
        'stress': 'svm'
    }

    def __init__(
        self,
        disease_name: str,
        random_state: int = 42,
        oversample: bool = False,
        algorithm: str = None
    ):
        """
        Initialize disease classifier.
        
        Args:
            disease_name: Name of disease to classify
            random_state: Random seed for reproducibility
            oversample: If True, randomly oversample the minority class inside
                each CV training fold (extension experiment). The paper did
                not balance the training data (Sec. 4.3), so the default is
                False.
            algorithm: 'lr', 'svm', 'rf' or 'gb'. Defaults to the best
                algorithm reported in Table 4 for this disease.
        """
        self.disease_name = disease_name
        self.random_state = random_state
        self.oversample = oversample
        if disease_name not in self.DISEASE_ALGORITHM:
            raise ValueError(
                f"Unknown disease '{disease_name}'. "
                f"Choose from: {list(self.DISEASE_ALGORITHM)}"
            )
        algorithm = algorithm or self.DISEASE_ALGORITHM[disease_name]
        if algorithm not in self.ALGORITHM_PARAM_GRIDS:
            raise ValueError(f"Unknown algorithm '{algorithm}'")
        self.config = {
            'algorithm': algorithm,
            'param_grid': self.ALGORITHM_PARAM_GRIDS[algorithm]
        }
        self.best_model = None
        self.best_params = None
        
    def _get_base_classifier(self):
        """Get base classifier based on disease configuration."""
        algo = self.config['algorithm']
        
        if algo == 'rf':
            return RandomForestClassifier(random_state=self.random_state)
        elif algo == 'gb':
            return GradientBoostingClassifier(random_state=self.random_state)
        elif algo == 'svm':
            return SVC(probability=True, random_state=self.random_state)
        elif algo == 'lr':
            return LogisticRegression(random_state=self.random_state, max_iter=1000)
        else:
            return RandomForestClassifier(random_state=self.random_state)
    
    def preprocess_data(
        self,
        df: pd.DataFrame,
        label_columns: list,
        test_size: float = 0.2
    ) -> Tuple:
        """
        Split raw data into train and test sets.

        Scaling and oversampling are NOT applied here. Both are fitted inside
        the model pipeline (see build_pipeline), so the test set never
        influences the scaler and duplicated minority samples never leak into
        cross-validation validation folds.
        
        Args:
            df: Input dataframe
            label_columns: List of all disease label columns
            test_size: Proportion of test set (paper: train 80% / test 20%)
            
        Returns:
            Tuple of (X_train, y_train, X_test, y_test, feature_names)
        """
        # Extract target and features
        y = df[self.disease_name]
        X = df.drop(label_columns, axis=1)
        
        # Train-test split on unscaled data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=self.random_state
        )
        
        return (
            X_train.values, y_train.values.astype(int),
            X_test.values, y_test.values.astype(int),
            X.columns
        )
    
    def build_pipeline(self) -> ImbPipeline:
        """
        Scaler -> (oversampler) -> classifier.

        In fit, the scaler is fitted on the training data only. If
        oversampling is enabled, the minority class is randomly oversampled
        (with replacement) to the size of the majority class. In GridSearchCV
        both steps are refitted separately inside each training fold;
        validation folds and the test set are only scaled, never oversampled.
        """
        steps = [('scaler', StandardScaler())]
        if self.oversample:
            steps.append(
                ('oversample', RandomOverSampler(random_state=self.random_state))
            )
        steps.append(('clf', self._get_base_classifier()))
        return ImbPipeline(steps)
    
    def train(
        self,
        X_train: np.ndarray,
        y_train: np.ndarray,
        cv_folds: int = 10
    ) -> Dict:
        """
        Train classifier with grid search.
        
        Args:
            X_train: Training features
            y_train: Training labels
            cv_folds: Number of cross-validation folds
            
        Returns:
            Dictionary with training results
        """
        # Setup cross-validation
        cv = StratifiedKFold(n_splits=cv_folds, shuffle=True, random_state=self.random_state)
        
        # Pipeline: scaling (and oversampling, if enabled) refitted per CV fold
        pipeline = self.build_pipeline()
        param_grid = {f'clf__{k}': v for k, v in self.config['param_grid'].items()}
        
        # Grid search (F1 of the positive class, same metric for every disease)
        grid_search = GridSearchCV(
            pipeline,
            param_grid,
            scoring='f1',
            cv=cv,
            n_jobs=-1,
            verbose=0
        )
        
        grid_search.fit(X_train, y_train)
        
        self.best_model = grid_search.best_estimator_
        self.best_params = {
            k.replace('clf__', '', 1): v for k, v in grid_search.best_params_.items()
        }
        
        return {
            'best_params': self.best_params,
            'best_score': grid_search.best_score_,
            'cv_results': grid_search.cv_results_
        }
    
    def evaluate(
        self,
        X_test: np.ndarray,
        y_test: np.ndarray
    ) -> Dict:
        """
        Evaluate model on test set.
        
        Args:
            X_test: Test features
            y_test: Test labels
            
        Returns:
            Dictionary with evaluation metrics
        """
        y_pred = self.best_model.predict(X_test)
        
        # Calculate metrics for the positive class (label 1), as in the paper
        precision, recall, f1, _ = precision_recall_fscore_support(
            y_test, y_pred, average='binary', pos_label=1, zero_division=0
        )
        
        # Confusion matrix (fixed label order: 0 = negative, 1 = positive)
        cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
        
        # Specificity (for binary classification)
        if cm.shape == (2, 2):
            tn, fp, fn, tp = cm.ravel()
            specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
        else:
            specificity = 0
        
        return {
            'precision': precision,
            'recall': recall,
            'f1_score': f1,
            'specificity': specificity,
            'confusion_matrix': cm,
            'predictions': y_pred
        }
    
    def get_feature_importance(self, feature_names) -> pd.DataFrame:
        """
        Extract feature importance from trained model.
        
        Args:
            feature_names: List of feature names
            
        Returns:
            DataFrame with feature importance sorted
        """
        clf = self.best_model.named_steps['clf']
        if hasattr(clf, 'feature_importances_'):
            importance_df = pd.DataFrame(
                clf.feature_importances_,
                index=feature_names,
                columns=['Importance']
            )
            return importance_df.sort_values(by='Importance', ascending=False).round(4)
        else:
            return pd.DataFrame()
    
    def plot_confusion_matrix(
        self,
        cm: np.ndarray,
        output_path: str = None
    ):
        """
        Plot and save confusion matrix.
        
        Args:
            cm: Confusion matrix
            output_path: Path to save figure
        """
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap="Blues", cbar=True)
        plt.title(f"Confusion Matrix: {self.disease_name.capitalize()}")
        plt.ylabel('Actual')
        plt.xlabel('Predicted')
        
        if output_path:
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            print(f"Confusion matrix saved to: {output_path}")
        
        plt.close()


def train_single_disease(
    disease_name: str,
    data_path: str,
    output_dir: str,
    random_state: int = 42,
    oversample: bool = False,
    select_algorithm: bool = False
):
    """
    Train classifier for a single disease.
    
    Args:
        disease_name: Name of disease
        data_path: Path to CSV data file
        output_dir: Directory to save results
        random_state: Random seed
        oversample: Oversample the minority class inside CV training folds
        select_algorithm: Compare LR/SVM/RF/GB by CV F1 on the training set
            and keep the best one, instead of using the Table 4 algorithm
    """
    print(f"\n{'='*60}")
    print(f"Training classifier for: {disease_name.upper()}")
    print(f"{'='*60}\n")
    
    # Create output directories
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    Path(f"{output_dir}/importances").mkdir(exist_ok=True)
    Path(f"{output_dir}/plots").mkdir(exist_ok=True)
    
    # Load data
    print("Loading data...")
    df = pd.read_csv(data_path)
    df.set_index(df.columns[0], inplace=True)
    
    # Rename columns to English
    df.rename(columns={
        '비만': 'obesity',
        '간장질환': 'liver',
        '고혈압': 'highpressure',
        '당뇨': 'diabete',
        '신장질환': 'kidney',
        '이상지질혈증': 'dyslipidemia',
        '기타흉부질환의심(순환기계질환)': 'circul',
        '근골격불균형': 'musculoskeletal',
        '스트레스주의': 'stress'
    }, inplace=True)
    
    label_columns = ['obesity', 'liver', 'highpressure', 'diabete', 
                     'kidney', 'dyslipidemia', 'circul', 'musculoskeletal', 'stress']
    
    # Initialize classifier (Table 4 algorithm unless selection is requested)
    classifier = DiseaseClassifier(disease_name, random_state, oversample)
    
    # Preprocess (split only; scaling/oversampling live in the pipeline)
    print("Preprocessing data...")
    X_train, y_train, X_test, y_test, feature_names = classifier.preprocess_data(
        df, label_columns
    )
    
    print(f"Training samples: {len(y_train)}, Test samples: {len(y_test)}")
    print(f"Class distribution (train): {np.bincount(y_train, minlength=2)}")
    if oversample:
        print("Oversampling: ON (minority class, inside each CV training fold only)")
    else:
        print("Oversampling: OFF (paper setting, Sec. 4.3)")
    
    # Train
    algorithm_cv_scores = {}
    if select_algorithm:
        # Paper-style comparison: all four algorithms, chosen by CV F1 on the
        # training set only (the test set is never used for selection)
        print("Comparing LR / SVM / RF / GB with grid search...")
        best = None
        for algo in DiseaseClassifier.ALGORITHM_PARAM_GRIDS:
            candidate = DiseaseClassifier(disease_name, random_state, oversample, algo)
            result = candidate.train(X_train, y_train)
            algorithm_cv_scores[algo] = round(float(result['best_score']), 4)
            print(f"  {algo.upper():>3}: CV F1 = {result['best_score']:.4f}  {result['best_params']}")
            if best is None or result['best_score'] > best[1]['best_score']:
                best = (candidate, result)
        classifier, train_results = best
    else:
        print("Training model with grid search...")
        train_results = classifier.train(X_train, y_train)
    print(f"Algorithm: {classifier.config['algorithm'].upper()}")
    print(f"Best parameters: {train_results['best_params']}")
    print(f"Best CV score: {train_results['best_score']:.4f}")
    
    # Evaluate
    print("\nEvaluating on test set...")
    eval_results = classifier.evaluate(X_test, y_test)
    
    print(f"\nTest Set Performance:")
    print(f"  Precision: {eval_results['precision']:.4f}")
    print(f"  Recall: {eval_results['recall']:.4f}")
    print(f"  F1-Score: {eval_results['f1_score']:.4f} ({eval_results['f1_score']*100:.2f}%)")
    print(f"  Specificity: {eval_results['specificity']:.4f}")
    
    # Save confusion matrix
    cm_path = f"{output_dir}/plots/{disease_name}_confusion_matrix.png"
    classifier.plot_confusion_matrix(eval_results['confusion_matrix'], cm_path)
    
    # Get and save feature importance
    importance_df = classifier.get_feature_importance(feature_names)
    if not importance_df.empty:
        importance_path = f"{output_dir}/importances/{disease_name}_feature_importance.xlsx"
        importance_df.to_excel(importance_path, index=True)
        print(f"\nFeature importance saved to: {importance_path}")
        print(f"\nTop 10 Important Features:")
        print(importance_df.head(10))
    
    # Save results summary
    results_summary = {
        'disease': disease_name,
        'experiment': 'oversample' if oversample else 'paper',
        'algorithm': classifier.config['algorithm'],
        'algorithm_selected_by_cv': select_algorithm,
        'algorithm_cv_scores': algorithm_cv_scores or None,
        'best_params': train_results['best_params'],
        'cv_score': train_results['best_score'],
        'test_precision': eval_results['precision'],
        'test_recall': eval_results['recall'],
        'test_f1': eval_results['f1_score'],
        'test_specificity': eval_results['specificity']
    }
    
    summary_df = pd.DataFrame([results_summary])
    summary_path = f"{output_dir}/{disease_name}_summary.csv"
    summary_df.to_csv(summary_path, index=False)
    print(f"\nResults summary saved to: {summary_path}")
    
    print(f"\n{'='*60}")
    print(f"Training completed for: {disease_name.upper()}")
    print(f"{'='*60}\n")
    
    return results_summary


def train_all_diseases(
    data_path: str,
    output_dir: str,
    random_state: int = 42,
    oversample: bool = False,
    select_algorithm: bool = False
):
    """
    Train classifiers for all diseases.
    
    Args:
        data_path: Path to CSV data file
        output_dir: Directory to save results
        random_state: Random seed
    """
    diseases = [
        'obesity', 'liver', 'highpressure', 'diabete', 
        'kidney', 'dyslipidemia', 'circul', 'musculoskeletal', 'stress'
    ]
    
    all_results = []
    
    for disease in diseases:
        try:
            result = train_single_disease(
                disease, data_path, output_dir, random_state,
                oversample, select_algorithm
            )
            all_results.append(result)
        except Exception as e:
            print(f"Error training {disease}: {str(e)}")
            continue
    
    # Save comprehensive results
    if all_results:
        all_results_df = pd.DataFrame(all_results)
        all_results_path = f"{output_dir}/all_diseases_summary.csv"
        all_results_df.to_csv(all_results_path, index=False)
        print(f"\nComprehensive results saved to: {all_results_path}")
        
        print("\n" + "="*80)
        print("FINAL RESULTS SUMMARY")
        print("="*80)
        print(all_results_df.to_string(index=False))


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description="Binary Relevance Multi-Label Disease Classifier"
    )
    parser.add_argument(
        '--disease',
        type=str,
        default='obesity',
        help='Disease to classify (or "all" for all diseases)'
    )
    parser.add_argument(
        '--data',
        type=str,
        default='data/health_data_total_proj1.csv',
        help='Path to data file'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='results',
        help='Output directory'
    )
    parser.add_argument(
        '--seed',
        type=int,
        default=42,
        help='Random seed'
    )
    parser.add_argument(
        '--oversample',
        action='store_true',
        help='Extension experiment: oversample the minority class inside '
             'each CV training fold (the paper did not balance the data)'
    )
    parser.add_argument(
        '--select-algorithm',
        action='store_true',
        help='Compare LR/SVM/RF/GB per disease by CV F1 instead of using '
             'the Table 4 algorithm'
    )
    
    args = parser.parse_args()
    
    # Keep the two experiments apart: results/paper/... vs results/oversample/...
    experiment = 'oversample' if args.oversample else 'paper'
    if args.select_algorithm:
        experiment += '_select'
    output_dir = str(Path(args.output) / experiment)
    
    # Set random seeds
    np.random.seed(args.seed)
    
    print("\n" + "="*80)
    print("BINARY RELEVANCE MULTI-LABEL HEALTH SCREENING CLASSIFIER")
    print("="*80)
    print(f"Data file: {args.data}")
    print(f"Output directory: {output_dir}")
    print(f"Random seed: {args.seed}")
    print(f"Experiment: {experiment}")
    
    if args.disease.lower() == 'all':
        train_all_diseases(
            args.data, output_dir, args.seed,
            args.oversample, args.select_algorithm
        )
    else:
        train_single_disease(
            args.disease.lower(), args.data, output_dir, args.seed,
            args.oversample, args.select_algorithm
        )
    
    print("\n" + "="*80)
    print("TRAINING COMPLETED SUCCESSFULLY!")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
