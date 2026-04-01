# Binary Relevance-based Multi-Label Classification for Occupational Health Screening

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Paper](https://img.shields.io/badge/Paper-KIIT%202024-red)](docs/paper.pdf)
[![DOI](https://img.shields.io/badge/DOI-10.14801%2Fjkiit.2024.22.2.43-blue)](http://dx.doi.org/10.14801/jkiit.2024.22.2.43)

> **📄 Research Paper**: [Binary-Relevance-based Multi-Label Classification using Medical Examination Data to Screen for Complex Illnesses in Construction and Manufacturing Workers](docs/paper.pdf)  
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
- **Class Imbalance Handling**: 오버샘플링을 통한 불균형 데이터 처리
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
- **[Full Paper PDF](docs/paper.pdf)** (Korean, included in this repository)
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
git clone https://github.com/yourusername/health-screening-ml.git
cd health-screening-ml
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1. Train Individual Disease Classifiers

각 질환별 분류기를 독립적으로 학습:

```bash
# Obesity Classifier
python obesity_importance_proj1.py

# Liver Disease Classifier
python liver_importance_proj1.py

# Hypertension Classifier
python highpressure_importance_proj1.py

# Diabetes Classifier
python diabete_importance_proj1.py

# Kidney Disease Classifier
python kidney_importance_proj1.py

# Dyslipidemia Classifier
python dyslipidemia_importance_proj1.py

# Cardiovascular Disease Classifier
python circul_importance_proj1.py
```

### 2. Output Files

각 스크립트는 다음을 생성합니다:
- **Feature Importance Excel**: `{disease}_all_importance.xlsx`
- **Confusion Matrix Plot**: `{disease}_n1.png`
- **Console Output**: F1-score, Best Hyperparameters

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

### Hyperparameter Ranges Tested

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
# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-Test Split (70-30)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42
)
```

### 2. Class Imbalance Handling
```python
# Oversample minority class
X_minority = X_train[y_train == 1]
y_minority = y_train[y_train == 1]

X_upsampled, y_upsampled = resample(
    X_minority, y_minority,
    replace=True,
    n_samples=(y_train == 0).sum(),
    random_state=42
)

X_resampled = np.vstack((X_train[y_train == 0], X_upsampled))
y_resampled = np.hstack((y_train[y_train == 0], y_upsampled))
```

### 3. Binary Relevance Approach

각 질환(레이블)에 대해 독립적인 이진 분류기를 학습:

```
For each disease d in D:
    1. Create binary dataset: X_d, y_d
    2. Handle class imbalance
    3. Grid search for optimal hyperparameters
    4. Train classifier_d with best params
    5. Evaluate on test set
    6. Extract feature importance
```

### 4. Model Selection & Evaluation
```python
# 10-Fold Stratified Cross-Validation
cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)

# Grid Search with F1-Score optimization
grid_search = GridSearchCV(
    clf, param_grid,
    scoring='f1',
    cv=cv,
    n_jobs=-1,
    verbose=0
)

grid_search.fit(X_resampled, y_resampled)
best_clf = grid_search.best_estimator_
```

---

## 📊 Feature Importance

각 질환별 상위 중요 특징이 Excel 파일로 저장됩니다:

### Example: Obesity Feature Importance
```
1. BMI (Body Mass Index)
2. Waist Circumference
3. Triglycerides
4. Weight
5. HDL Cholesterol
...
```

Excel 파일 경로: `result_importances/{disease}_all_importance.xlsx`

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
논문에 포함된 ROC 곡선으로 모델 성능을 시각화합니다.

---

## 📝 Project Structure

```
health-screening-ml/
├── README.md                           # This file
├── requirements.txt                    # Python dependencies
├── LICENSE                             # MIT License
├── .gitignore                          # Git ignore rules
│
├── train_classifier.py                 # Unified training script
├── QUICKSTART.md                       # Quick start guide
├── CONTRIBUTING.md                     # Contribution guidelines
│
├── scripts/                            # Original classification scripts
│   ├── obesity_importance_proj1.py
│   ├── liver_importance_proj1.py
│   ├── highpressure_importance_proj1.py
│   ├── diabete_importance_proj1.py
│   ├── kidney_importance_proj1.py
│   ├── dyslipidemia_importance_proj1.py
│   ├── circul_importance_proj1.py
│   └── obesity_score.py
│
├── docs/                               # Documentation
│   └── paper.pdf                       # Research paper (KIIT 2024)
│
└── data/                               # Data directory (NOT included - IRB protected)
    └── health_data_total_proj1.csv    # Dataset (obtain separately)
```

**Note**: 
- `data/` folder is excluded via `.gitignore` (IRB protected)
- `results/` folder is auto-generated when running scripts
- Add your own `data/health_data_total_proj1.csv` to run the code

---

## 🔍 Key Insights

### 1. High Performance Diseases
- **Obesity** (F1: 0.85): 비만은 BMI, 허리둘레 등 명확한 지표로 높은 정확도
- **Musculoskeletal Imbalance** (F1: 0.84): 근골격 불균형도 높은 예측 성능
- **Liver Disease** (F1: 0.77): 간 효소 지표로 양호한 성능

### 2. Challenging Diseases
- **Diabetes** (F1: 0.00): 샘플 수 부족으로 예측 실패
- **Dyslipidemia** (F1: 0.00): 데이터 불균형 심각
- **Cardiovascular** (F1: 0.00): 추가 특징 엔지니어링 필요

### 3. Model Selection Patterns
- **Random Forest**: 비만 (안정적 성능)
- **Gradient Boosting**: 대부분 질환 (높은 정확도)
- **SVM**: 스트레스 (비선형 패턴 포착)
- **Logistic Regression**: 순환기 질환 (단순 선형 관계)

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

### Key Literature
1. **Binary Relevance**: Zhang & Zhou (2014) - "A Review on Multi-Label Learning Algorithms"
2. **Random Forests**: Breiman (2001) - "Random Forests"
3. **Gradient Boosting**: Friedman (2001) - "Greedy Function Approximation"
4. **Class Imbalance**: Chawla et al. (2002) - "SMOTE: Synthetic Minority Over-sampling"

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

- **Teh-Hao Teng** - Master's Student, Sungkyunkwan University
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
