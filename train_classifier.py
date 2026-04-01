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
    python train_classifier.py --disease obesity --output_dir results/
    python train_classifier.py --disease all --output_dir results/
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
from sklearn.utils import resample
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
    
    DISEASE_CONFIG = {
        'obesity': {
            'algorithm': 'rf',
            'param_grid': {
                'n_estimators': [70, 80, 90],
                'min_samples_leaf': [1, 2]
            }
        },
        'liver': {
            'algorithm': 'gb',
            'param_grid': {
                'n_estimators': [30, 40, 50],
                'max_features': ['sqrt'],
                'max_depth': [9, 10, 11],
                'min_samples_split': [2, 3, 4],
                'min_samples_leaf': [1, 2]
            }
        },
        'highpressure': {
            'algorithm': 'gb',
            'param_grid': {
                'n_estimators': [10, 20, 30],
                'max_depth': [7, 8, 9, 10, 12],
                'min_samples_split': [1, 2, 3, 4, 5],
                'min_samples_leaf': [1, 2, 3, 4]
            }
        },
        'diabete': {
            'algorithm': 'gb',
            'param_grid': {
                'n_estimators': [10, 20],
                'min_samples_leaf': [1, 2, 3]
            }
        },
        'kidney': {
            'algorithm': 'gb',
            'param_grid': {
                'n_estimators': [30, 40, 50],
                'max_features': ['sqrt'],
                'max_depth': [5, 6, 7],
                'min_samples_split': [1, 2, 3],
                'min_samples_leaf': [1, 2]
            }
        },
        'dyslipidemia': {
            'algorithm': 'gb',
            'param_grid': {
                'n_estimators': [40, 50, 60],
                'min_samples_leaf': [1, 2]
            }
        },
        'circul': {
            'algorithm': 'gb',
            'param_grid': {
                'n_estimators': [10, 20],
                'min_samples_leaf': [1, 2]
            }
        },
        'musculoskeletal': {
            'algorithm': 'gb',
            'param_grid': {
                'learning_rate': [0.001],
                'min_samples_split': [2],
                'n_estimators': [50]
            }
        },
        'stress': {
            'algorithm': 'svm',
            'param_grid': {
                'C': [10],
                'gamma': ['scale'],
                'kernel': ['sigmoid']
            }
        }
    }
    
    def __init__(self, disease_name: str, random_state: int = 42):
        """
        Initialize disease classifier.
        
        Args:
            disease_name: Name of disease to classify
            random_state: Random seed for reproducibility
        """
        self.disease_name = disease_name
        self.random_state = random_state
        self.config = self.DISEASE_CONFIG.get(disease_name, self.DISEASE_CONFIG['obesity'])
        self.scaler = StandardScaler()
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
        test_size: float = 0.3
    ) -> Tuple:
        """
        Preprocess data: scaling, train-test split, oversampling.
        
        Args:
            df: Input dataframe
            label_columns: List of all disease label columns
            test_size: Proportion of test set
            
        Returns:
            Tuple of (X_resampled, y_resampled, X_test, y_test)
        """
        # Extract target and features
        y = df[self.disease_name]
        X = df.drop(label_columns, axis=1)
        
        # Scale features
        X_scaled = self.scaler.fit_transform(X)
        
        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=test_size, random_state=self.random_state
        )
        
        # Convert to DataFrames for easier handling
        X_train = pd.DataFrame(X_train).reset_index(drop=True)
        y_train = pd.Series(y_train).reset_index(drop=True)
        X_test = pd.DataFrame(X_test).reset_index(drop=True)
        y_test = pd.Series(y_test).reset_index(drop=True)
        
        # Handle class imbalance with oversampling
        X_minority = X_train[y_train == 1]
        y_minority = y_train[y_train == 1]
        
        if len(y_minority) > 0:
            X_upsampled, y_upsampled = resample(
                X_minority, y_minority,
                replace=True,
                n_samples=(y_train == 0).sum(),
                random_state=self.random_state
            )
            
            X_resampled = np.vstack((X_train[y_train == 0], X_upsampled))
            y_resampled = np.hstack((y_train[y_train == 0], y_upsampled))
        else:
            X_resampled = X_train.values
            y_resampled = y_train.values
        
        return X_resampled, y_resampled, X_test.values, y_test.values, X.columns
    
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
        
        # Get base classifier
        base_clf = self._get_base_classifier()
        
        # Determine scoring metric
        scoring = 'f1_weighted' if self.config['algorithm'] == 'gb' and self.disease_name == 'circul' else 'f1'
        
        # Grid search
        grid_search = GridSearchCV(
            base_clf,
            self.config['param_grid'],
            scoring=scoring,
            cv=cv,
            n_jobs=-1,
            verbose=0
        )
        
        grid_search.fit(X_train, y_train)
        
        self.best_model = grid_search.best_estimator_
        self.best_params = grid_search.best_params_
        
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
        
        # Calculate metrics
        precision, recall, f1, _ = precision_recall_fscore_support(
            y_test, y_pred, average='weighted', zero_division=0
        )
        
        # Confusion matrix
        cm = confusion_matrix(y_test, y_pred)
        
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
        if hasattr(self.best_model, 'feature_importances_'):
            importance_df = pd.DataFrame(
                self.best_model.feature_importances_,
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
    random_state: int = 42
):
    """
    Train classifier for a single disease.
    
    Args:
        disease_name: Name of disease
        data_path: Path to CSV data file
        output_dir: Directory to save results
        random_state: Random seed
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
    
    # Initialize classifier
    classifier = DiseaseClassifier(disease_name, random_state)
    
    # Preprocess
    print("Preprocessing data...")
    X_train, y_train, X_test, y_test, feature_names = classifier.preprocess_data(
        df, label_columns
    )
    
    print(f"Training samples: {len(y_train)}, Test samples: {len(y_test)}")
    print(f"Class distribution (train): {np.bincount(y_train.astype(int))}")
    
    # Train
    print("Training model with grid search...")
    train_results = classifier.train(X_train, y_train)
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
    random_state: int = 42
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
            result = train_single_disease(disease, data_path, output_dir, random_state)
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
    
    args = parser.parse_args()
    
    # Set random seeds
    np.random.seed(args.seed)
    
    print("\n" + "="*80)
    print("BINARY RELEVANCE MULTI-LABEL HEALTH SCREENING CLASSIFIER")
    print("="*80)
    print(f"Data file: {args.data}")
    print(f"Output directory: {args.output}")
    print(f"Random seed: {args.seed}")
    
    if args.disease.lower() == 'all':
        train_all_diseases(args.data, args.output, args.seed)
    else:
        train_single_disease(args.disease.lower(), args.data, args.output, args.seed)
    
    print("\n" + "="*80)
    print("TRAINING COMPLETED SUCCESSFULLY!")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
