# Quick Start Guide

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/health-screening-ml.git
cd health-screening-ml

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Data Preparation

1. **Obtain Data**: Due to IRB restrictions, you need to prepare your own data
2. **Format**: CSV file with the following structure:

```csv
Index,Feature1,Feature2,...,Feature82,obesity,liver,highpressure,diabete,kidney,dyslipidemia,circul,musculoskeletal,stress
001,25.3,120,80,...,1,0,0,0,0,1,0,0,0
002,22.1,115,75,...,0,0,0,0,0,0,0,0,0
...
```

3. **Place Data**: Save as `data/health_data_total_proj1.csv`

## Running the Code

### Train Single Disease Classifier

```bash
# Train obesity classifier
python train_classifier.py --disease obesity --data data/health_data_total_proj1.csv --output results/

# Train liver disease classifier
python train_classifier.py --disease liver --output results/

# Train all other diseases...
```

### Train All Diseases at Once

```bash
python train_classifier.py --disease all --data data/health_data_total_proj1.csv --output results/
```

### Command Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `--disease` | Disease to classify (`obesity`, `liver`, etc. or `all`) | `obesity` |
| `--data` | Path to CSV data file | `data/health_data_total_proj1.csv` |
| `--output` | Output directory for results | `results` |
| `--seed` | Random seed for reproducibility | `42` |

## Expected Output

After running, you'll get:

```
results/
├── importances/
│   ├── obesity_feature_importance.xlsx
│   ├── liver_feature_importance.xlsx
│   └── ...
├── plots/
│   ├── obesity_confusion_matrix.png
│   ├── liver_confusion_matrix.png
│   └── ...
├── obesity_summary.csv
├── liver_summary.csv
├── ...
└── all_diseases_summary.csv  # If you ran --disease all
```

## Sample Output

```
============================================================
Training classifier for: OBESITY
============================================================

Loading data...
Preprocessing data...
Training samples: 840, Test samples: 121
Class distribution (train): [420 420]
Training model with grid search...
Best parameters: {'min_samples_leaf': 1, 'n_estimators': 80}
Best CV score: 0.8234

Evaluating on test set...

Test Set Performance:
  Precision: 0.9583
  Recall: 0.7667
  F1-Score: 0.8519 (85.19%)
  Specificity: 0.9890

Confusion matrix saved to: results/plots/obesity_confusion_matrix.png
Feature importance saved to: results/importances/obesity_feature_importance.xlsx

Top 10 Important Features:
                    Importance
BMI                    0.2453
Waist                  0.1892
Triglycerides          0.1234
Weight                 0.0987
HDL                    0.0765
...

Results summary saved to: results/obesity_summary.csv

============================================================
Training completed for: OBESITY
============================================================
```

## Using Original Scripts

If you prefer the original individual scripts:

```bash
# Make sure data file is in the same directory or update path in script
python obesity_importance_proj1.py
python liver_importance_proj1.py
# ... etc
```

## Troubleshooting

### Data File Not Found
```
Error: FileNotFoundError: data/health_data_total_proj1.csv
```
**Solution**: Make sure your data file exists at the specified path

### Missing Columns
```
Error: KeyError: 'obesity'
```
**Solution**: Check that your CSV has the correct disease column names in Korean or English

### Memory Error
```
Error: MemoryError
```
**Solution**: Reduce the parameter grid or use fewer cross-validation folds

### Poor Performance
If you get F1-score of 0.0000:
- Check class balance (might have too few positive samples)
- Try adjusting hyperparameter ranges
- Consider using SMOTE instead of simple oversampling

## Next Steps

1. **Analyze Results**: Check confusion matrices and feature importance
2. **Tune Models**: Adjust hyperparameter grids in `train_classifier.py`
3. **Experiment**: Try different algorithms or ensemble methods
4. **Validate**: Use k-fold cross-validation results to assess stability

## Getting Help

- **Issues**: Open an issue on GitHub
- **Email**: mtchoi@skku.edu
- **Documentation**: See full README.md
