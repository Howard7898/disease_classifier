# Binary Relevance-based Multi-Label Classification for Occupational Health Screening

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Paper](https://img.shields.io/badge/Paper-KIIT%202024-red)](https://doi.org/10.14801/jkiit.2024.22.2.43)
[![DOI](https://img.shields.io/badge/DOI-10.14801%2Fjkiit.2024.22.2.43-blue)](http://dx.doi.org/10.14801/jkiit.2024.22.2.43)

> **📄 Research Paper**: [Binary-Relevance-based Multi-Label Classification using Medical Examination Data to Screen for Complex Illnesses in Construction and Manufacturing Workers](https://www.ki-it.com/xml/39836/39836.pdf)  
> **Published in**: Journal of KIIT, Vol. 22, No. 2, pp. 43-52, February 2024  
> **Authors**: Teh-Hao Teng, Tae-Rim Lee, Seung Hyeok Byeon, Mun-Taek Choi

## 📋 Overview

건설 및 제조 현장 작업자의 **복합 질환 선별**을 위한 Binary Relevance 기반 다중 레이블 분류 시스템입니다. 601명의 작업자로부터 수집된 건강 검진 데이터(82개 특징)를 활용하여 9가지 주요 질환을 예측합니다.

This project implements a **Binary Relevance-based Multi-Label Classification** system to screen complex illnesses in construction and manufacturing workers using medical examination data from 601 workers (82 features) to predict 9 major diseases.

### 🎯 Key Features

- **Multi-Label Classification**: 한 사람이 여러 질환을 동시에 가질 수 있는 현실적인 시나리오 반영
- **Binary Relevance Approach**: 각 질환별 독립적인 이진 분류기 학습
- **Advanced ML Algorithms**: Random Forest, Gradient Boosting, SVM, Logistic Regression
- **Hyperparameter Optimization**: GridSearchCV를 통한 자동 튜닝
- **Leak-free Evaluation**: 스케일링(및 선택 시 오버샘플링)을 교차검증 학습 폴드 안에서만 학습
- **Two Experiment Modes**: 논문 재현(오버샘플링 없음) / 추가 개선(폴드 내부 오버샘플링)
- **Feature Importance Analysis**: 각 질환별 주요 건강 지표 분석

---

## 📑 Publication

This repository contains the implementation of the research published in:

**Title**: Binary-Relevance-based Multi-Label Classification using Medical Examination Data to Screen for Complex Illnesses in Construction and Manufacturing Workers  
**Journal**: Journal of the Korea Institute of Information Technology (KIIT)  
**Volume**: 22, Issue 2, Pages 43-52  
**Published**: February 28, 2024  
**DOI**: [10.14801/jkiit.2024.22.2.43](http://dx.doi.org/10.14801/jkiit.2024.22.2.43)

### 📥 Access the Paper
- **[Full Paper PDF](https://www.ki-it.com/xml/39836/39836.pdf)** (Korean, journal website)
- **[Journal Website](http://dx.doi.org/10.14801/jkiit.2024.22.2.43)** (Official publication)

### ✍️ Citation
If you use this code or methodology in your research, please cite:

```bibtex
@article{teng2024binary,
  title={건설-제조 현장 작업자의 복합 질환 선별을 위한 건강 검진 데이터를 사용한 이진-관련성-기반 다중 레이블 분류},
  author={등덕호 and 이태림 and 변승혁 and 최문택},
  journal={Journal of KIIT},
  volume={22},
  number={2},
  pages={43--52},
  year={2024},
  month={2},
  publisher={한국정보기술학회},
  doi={10.14801/jkiit.2024.22.2.43}
}
```

**English Citation**:
```
Teng, T.-H., Lee, T.-R., Byeon, S. H., & Choi, M.-T. (2024). 
Binary-Relevance-based Multi-Label Classification using Medical Examination Data 
to Screen for Complex Illnesses in Construction and Manufacturing Workers. 
Journal of KIIT, 22(2), 43-52. doi:10.14801/jkiit.2024.22.2.43
```

---

## 🏥 Target Diseases (질환 레이블)

| Korean Name | English Name | Label Code |
|------------|--------------|------------|
| 비만 | Obesity | `obesity` |
| 간장질환 | Liver Disease | `liver` |
| 고혈압 | Hypertension | `highpressure` |
| 당뇨 | Diabetes | `diabete` |
| 신장질환 | Kidney Disease | `kidney` |
| 이상지질혈증 | Dyslipidemia | `dyslipidemia` |
| 순환기계질환 | Cardiovascular Disease | `circul` |
| 근골격불균형 | Musculoskeletal Imbalance | `musculoskeletal` |
| 스트레스주의 | Stress | `stress` |

---

## 📊 Dataset

### Data Characteristics
- **Total Samples**: 601 workers
- **Features**: 82 health examination metrics
- **Labels**: 9 disease categories (binary)
- **Collection Period**: April 2021 - December 2023
- **Source**: Hanshin Medipia Medical Examinations

### Key Health Features
```
- Body Mass Index (BMI)
- Blood Pressure (Diastolic/Systolic)
- Waist Circumference
- Triglycerides
- HDL Cholesterol
- HbA1c (Diabetes indicator)
- Creatinine (Kidney function)
- Liver enzymes (AST, ALT, GGT)
- Uric Acid
- And 70+ more clinical metrics...
```

### Data Format
```csv
Index, Feature1, Feature2, ..., Feature82, obesity, liver, highpressure, diabete, kidney, dyslipidemia, circul, musculoskeletal, stress
```

**Note**: Due to privacy regulations (IRB approval: HS23-3), actual dataset is not included in this repository.

---

## 🛠️ Installation

### Prerequisites
```bash
Python >= 3.8
```

### Clone Repository
```bash
git clone https://github.com/Howard7898/disease_classifier.git
cd disease_classifier
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1. Train a Classifier

`train_classifier.py` trains one binary classifier per disease (Binary Relevance). Each disease uses the best algorithm reported in Table 4 of the paper, tuned by grid search over that algorithm's range in Table 3.

```bash
# One disease (e.g., obesity, liver, highpressure, diabete, kidney, dyslipidemia, circul)
python train_classifier.py --disease obesity --data data/health_data_total_proj1.csv --output results

# All diseases at once
python train_classifier.py --disease all --data data/health_data_total_proj1.csv --output results
```

### 2. Experiment Modes

| Experiment | Command flag | Setting | Output folder |
|---|---|---|---|
| Paper reproduction (default) | — | No class balancing, as stated in the paper (Sec. 4.3) | `results/paper/` |
| Extension | `--oversample` | Random oversampling of the minority class **inside each CV training fold only** | `results/oversample/` |
| Optional algorithm comparison | `--select-algorithm` | Grid-searches LR, SVM, RF and GB per disease and keeps the best by CV F1 on the training set | `results/<mode>_select/` |

The paper's original experiment did not oversample, so results from `--oversample` are an additional experiment and should not be reported as reproductions of Table 4. The default run uses the Table 4 algorithm per disease; `--select-algorithm` re-runs the comparison step (the test set is never used for selection).

### 3. Output Files

- **Confusion matrix**: `results/<mode>/plots/{disease}_confusion_matrix.png`
- **Feature importance**: `results/<mode>/importances/{disease}_feature_importance.xlsx`
- **Summary**: `results/<mode>/{disease}_summary.csv`, `results/<mode>/all_diseases_summary.csv`
- **Console output**: F1-score, precision, recall (positive class), specificity, best hyperparameters

---

## 📈 Model Performance

### Best Performing Models (Test Set Results)

| Disease | Best Algorithm | F1-Score | Precision | Recall | Specificity |
|---------|---------------|----------|-----------|--------|-------------|
| **Obesity** | Random Forest | **0.8519** | 0.9583 | 0.7667 | 0.9890 |
| **Liver Disease** | Gradient Boosting | **0.7692** | 0.8824 | 0.6818 | 0.9798 |
| **Hypertension** | Gradient Boosting | **0.6250** | 0.7143 | 0.5556 | 0.9821 |
| **Kidney Disease** | Gradient Boosting | **0.7368** | 1.0000 | 0.5833 | 1.0000 |
| **Musculoskeletal** | Gradient Boosting | **0.8421** | 0.7273 | 1.0000 | 0.0000 |
| **Stress** | SVM | **0.3188** | 0.3438 | 0.2973 | 0.7500 |
| Diabetes | Gradient Boosting | 0.0000 | 0.0000 | 0.0000 | 0.9744 |
| Dyslipidemia | Gradient Boosting | 0.0000 | 0.0000 | 0.0000 | 0.9744 |
| Cardiovascular | Logistic Regression | 0.0000 | 0.0000 | 0.0000 | 0.9832 |

### Hyperparameter Ranges Tested (Table 3)

#### Random Forest (RF)
```python
{
    'n_estimators': [100, 150, 200],
    'min_samples_leaf': [1, 2, 3]
}
```

#### Gradient Boosting (GB)
```python
{
    'learning_rate': [0.001, 0.01, 0.1],
    'min_samples_split': [2, 3, 4],
    'n_estimators': [50, 100, 150]
}
```

#### Support Vector Machine (SVM)
```python
{
    'C': [0.1, 1, 10],
    'kernel': ['poly', 'rbf', 'sigmoid'],
    'gamma': ['scale', 'auto']
}
```

#### Logistic Regression (LR)
```python
{
    'C': [0.01, 0.1, 1],
    'solver': ['newton-cg', 'lbfgs', 'liblinear']
}
```

---

## 🔬 Methodology

### 1. Data Preprocessing
```python
# Train-Test Split (80-20) on the raw (unscaled) data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```
Scaling is **not** applied to the full dataset. The scaler is part of the model pipeline and is fitted only on training data, so the test set (and each CV validation fold) never influences it.

### 2. Pipeline: Scaling and (optional) Oversampling
```python
from imblearn.pipeline import Pipeline as ImbPipeline
from imblearn.over_sampling import RandomOverSampler

steps = [('scaler', StandardScaler())]
if oversample:                       # --oversample (extension experiment)
    steps.append(('oversample', RandomOverSampler(random_state=42)))
steps.append(('clf', classifier))
pipeline = ImbPipeline(steps)
```
With `--oversample`, the minority class is duplicated (sampling with replacement) up to the size of the majority class **inside each training fold**. Validation folds and the test set are only scaled, never oversampled, so duplicated samples cannot appear on both sides of a split.

### 3. Binary Relevance Approach

각 질환(레이블)에 대해 독립적인 이진 분류기를 학습:

```
For each disease d in D:
    1. Create binary dataset: X_d, y_d
    2. Split into train (80%) / test (20%)
    3. Grid search over the pipeline with Stratified K-Fold CV on the training set
       (scaler, and oversampler if enabled, refitted in every training fold)
    4. Refit the best pipeline on the full training set
    5. Evaluate once on the held-out test set
    6. Extract feature importance (tree-based models)
```

### 4. Model Selection & Evaluation
```python
# Stratified K-Fold on the training set (the paper states K-fold; this code uses K=10)
cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)

# Grid Search with F1-Score (positive class) optimization
param_grid = {f'clf__{k}': v for k, v in table3_grid.items()}
grid_search = GridSearchCV(
    pipeline, param_grid,
    scoring='f1',
    cv=cv,
    n_jobs=-1,
    verbose=0
)

grid_search.fit(X_train, y_train)          # raw training data, no pre-scaling
best_clf = grid_search.best_estimator_     # scaler fitted on training data only

# Test-set metrics for the positive class (label 1)
precision, recall, f1, _ = precision_recall_fscore_support(
    y_test, best_clf.predict(X_test), average='binary', pos_label=1, zero_division=0
)
```

---

## 📊 Feature Importance

트리 기반 모델(RF, GB)을 사용하는 질환은 특징 중요도가 Excel 파일로 저장됩니다. 중요도 순위는 실행 결과에 따라 결정되며, 논문에는 질환별 특징 중요도 순위가 보고되어 있지 않습니다.

Excel 파일 경로: `results/<mode>/importances/{disease}_feature_importance.xlsx`

---

## 🎨 Visualizations

### Confusion Matrix
각 질환별 혼동 행렬이 자동으로 생성됩니다:

```
             Predicted
             N      P
Actual  N   TN     FP
        P   FN     TP
```

### ROC-AUC Curves
논문 그림 2에 질환별 ROC-AUC 곡선이 제시되어 있습니다. 현재 `train_classifier.py`는 ROC 곡선을 생성하지 않으며, 혼동 행렬만 저장합니다.

---

## 📝 Project Structure

```
disease_classifier/
├── README.md             # This file
├── QUICKSTART.md         # Short run guide
├── requirements.txt      # Python dependencies
├── LICENSE               # MIT License
├── train_classifier.py   # Training · evaluation · feature importance (all diseases)
└── data/                 # NOT included (IRB protected) — place health_data_total_proj1.csv here
```

**Note**: the dataset is not distributed (IRB approval HS23-3). `results/` is created automatically when the script runs.

---

## 🔍 Key Insights

아래 내용은 논문 표 4와 4.2·4.3절의 결과를 요약한 것입니다.

### 1. 양성 예측이 비교적 양호한 질환
- **Obesity** (RF, F1: 0.8519, SP: 0.9890): 양성과 음성 모두 높은 수준으로 예측
- **Liver Disease** (GB, F1: 0.7692, SP: 0.9798)
- **Kidney Disease** (GB, F1: 0.7368, SP: 1.0000)

### 2. 해석에 주의가 필요한 질환
- **Musculoskeletal Imbalance** (GB, F1: 0.8421, SP: 0.0000): 양성은 모두 맞혔지만(Recall 1.0000) 음성은 하나도 맞히지 못함. 사실상 대부분을 양성으로 예측한 결과로, F1만으로 성능이 높다고 보기 어려움

### 3. 양성 예측이 낮은 질환
- **Diabetes**, **Dyslipidemia**, **Cardiovascular** (F1: 0.0000): 양성은 하나도 맞히지 못했지만 음성 예측(SP)은 0.97 이상
- **Stress** (SVM, F1: 0.3188), **Hypertension** (GB, F1: 0.6250)

### 4. 종합 (논문 4.3절)
- 양성 예측률이 낮은 질환이 많아 실제 임상 적용에는 충분하지 않은 수준
- 음성 예측 성능은 매우 높은 편이어서 초기 분석 모델로서 의미가 있음
- 수집된 데이터는 레이블 간 불균형 상태이며, 혼동 행렬을 제시한 비만·간 질환·고혈압(표 5~7)에서는 양성 데이터가 음성보다 크게 적음
- LR·SVM·RF·GB를 그리드 서치로 학습하고, 최적 파라미터를 적용한 모델의 성능을 테스트 세트 기준으로 평가해 질환별 최고 모델을 표 4에 제시

---

## ⚠️ Limitations & Future Work

### Current Limitations
1. **Small Dataset**: 601 samples → 더 많은 데이터 필요
2. **Class Imbalance**: 일부 질환의 양성 샘플 극히 부족
3. **Label Independence**: BR 방법은 질환 간 상관관계 무시
4. **Feature Engineering**: 도메인 전문가와 협업 필요

### Future Improvements
- [ ] **Classifier Chains** or **Label Powerset**: 레이블 간 의존성 고려
- [ ] **SMOTE** (Synthetic Minority Over-sampling): 더 정교한 오버샘플링
- [ ] **Deep Learning**: Multi-Label Neural Networks
- [ ] **Ensemble Methods**: 여러 BR 모델 결합
- [ ] **Feature Selection**: Recursive Feature Elimination
- [ ] **Data Augmentation**: GAN을 통한 합성 데이터 생성

---

## 📚 References

### Academic Paper
```bibtex
@article{teng2024binary,
  title={Binary-Relevance-based Multi-Label Classification using Medical Examination Data to Screen for Complex Illnesses in Construction and Manufacturing Workers},
  author={Teng, Teh-Hao and Lee, Tae-Rim and Byeon, Seung Hyeok and Choi, Mun-Taek},
  journal={Journal of KIIT},
  volume={22},
  number={2},
  pages={43--52},
  year={2024},
  publisher={Korea Institute of Information Technology},
  doi={10.14801/jkiit.2024.22.2.43}
}
```

### Key Literature (cited in the paper)
1. **Binary Relevance** [8]: Alvares-Cherman, Metz & Monard (2012) - "Incorporating label dependency into the binary relevance framework for multi-label classification", *Expert Systems with Applications*
2. **Logistic Regression** [10]: Dreiseitl & Ohno-Machado (2002) - "Logistic regression and artificial neural network classification models: a methodology review", *Journal of Biomedical Informatics*
3. **Support Vector Machines** [11]: Awad & Khanna (2015) - "Support vector machines for classification", *Efficient Learning Machines*
4. **Random Forests** [12]: Breiman (2001) - "Random forests", *Machine Learning*
5. **Gradient Boosting** [13]: Friedman (2002) - "Stochastic gradient boosting", *Computational Statistics & Data Analysis*
6. **Imbalanced Multi-Label Classification** [5]: Tarekegn, Giacobini & Michalak (2021) - "A review of methods for imbalanced multi-label classification", *Pattern Recognition*

Numbers in brackets are the reference numbers in the paper.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

- **Teh-Hao Teng** - M.S. in Intelligent Robotics, Sungkyunkwan University (2025) (first author)
- **Tae-Rim Lee** - Ph.D. Student, Sungkyunkwan University
- **Seung Hyeok Byeon** - R&D Director, InfinityCare Inc.
- **Mun-Taek Choi** - Professor, Sungkyunkwan University (Corresponding Author)

---

## 📧 Contact

For questions or collaborations, please contact:
- **Email**: mtchoi@skku.edu
- **Institution**: Sungkyunkwan University, Department of Intelligent Robotics

---

## 🙏 Acknowledgments

- 한신메디피아 (Hanshin Medipia) for providing medical examination data
- 산업통상자원부 및 산업기술평가관리원 (KEIT) for research funding (Project No. 20015190)
- IRB Approval: HS23-3 (April 12, 2023)

---

## 📊 Citation

If you use this code or methodology in your research, please cite:

```
Teng, T.-H., Lee, T.-R., Byeon, S. H., & Choi, M.-T. (2024). 
Binary-Relevance-based Multi-Label Classification using Medical Examination Data 
to Screen for Complex Illnesses in Construction and Manufacturing Workers. 
Journal of KIIT, 22(2), 43-52. doi:10.14801/jkiit.2024.22.2.43
```

---

**Last Updated**: April 2026  
**Version**: 1.0.0  
**Status**: Research Project
