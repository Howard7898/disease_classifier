# Contributing to Health Screening ML

Thank you for your interest in contributing to this project! 🎉

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, Python version, etc.)

### Suggesting Enhancements

We welcome suggestions for:
- New features
- Performance improvements
- Better documentation
- Alternative algorithms

Please open an issue with:
- Clear description of the enhancement
- Use case / motivation
- Potential implementation approach

### Pull Requests

1. **Fork the Repository**
   ```bash
   git clone https://github.com/yourusername/health-screening-ml.git
   cd health-screening-ml
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**
   - Write clear, documented code
   - Follow PEP 8 style guidelines
   - Add tests if applicable
   - Update documentation

4. **Test Your Changes**
   ```bash
   # Run existing tests
   pytest tests/
   
   # Check code style
   flake8 .
   black --check .
   ```

5. **Commit**
   ```bash
   git add .
   git commit -m "Add: clear description of changes"
   ```

6. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then open a Pull Request on GitHub

## Code Style

### Python Style Guide
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and small

### Example
```python
def calculate_f1_score(precision: float, recall: float) -> float:
    """
    Calculate F1-score from precision and recall.
    
    Args:
        precision: Precision value (0-1)
        recall: Recall value (0-1)
        
    Returns:
        F1-score (0-1)
        
    Raises:
        ValueError: If precision or recall are invalid
    """
    if precision < 0 or recall < 0:
        raise ValueError("Precision and recall must be non-negative")
    
    if precision + recall == 0:
        return 0.0
        
    return 2 * (precision * recall) / (precision + recall)
```

## Areas for Contribution

### High Priority
- [ ] Implement Classifier Chains for label dependency
- [ ] Add SMOTE for better class imbalance handling
- [ ] Create visualization dashboard
- [ ] Add unit tests
- [ ] Improve documentation

### Medium Priority
- [ ] Implement deep learning models
- [ ] Add feature selection methods
- [ ] Create Docker container
- [ ] Add CI/CD pipeline
- [ ] Benchmarking suite

### Low Priority (Nice to Have)
- [ ] Web interface
- [ ] REST API
- [ ] Mobile app integration
- [ ] Real-time prediction service

## Development Setup

```bash
# Install development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run tests
pytest tests/ -v

# Check coverage
pytest --cov=src tests/
```

## Commit Message Guidelines

Use clear, descriptive commit messages:

```
Add: New feature
Fix: Bug fix
Update: Changes to existing functionality
Docs: Documentation changes
Test: Adding or updating tests
Refactor: Code refactoring
Style: Code style changes
```

Examples:
```
Add: Implement Classifier Chains method
Fix: Resolve class imbalance in kidney disease
Update: Improve feature scaling method
Docs: Add API documentation
Test: Add unit tests for DiseaseClassifier
```

## Code Review Process

All submissions require review. We use GitHub Pull Requests for this purpose.

### Review Checklist
- [ ] Code follows style guidelines
- [ ] Documentation is updated
- [ ] Tests pass
- [ ] No breaking changes (or clearly documented)
- [ ] Commit messages are clear

## Research Contributions

If you're contributing research improvements:

1. **Document Your Approach**
   - Theoretical background
   - Experimental setup
   - Results comparison

2. **Provide Evidence**
   - Performance metrics
   - Statistical tests
   - Ablation studies

3. **Reproducibility**
   - Set random seeds
   - Document hyperparameters
   - Provide sample results

## Questions?

Feel free to:
- Open an issue for discussion
- Email: mtchoi@skku.edu
- Check existing issues and PRs

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Acknowledgments

Contributors will be acknowledged in:
- README.md
- Research papers (if applicable)
- Release notes

Thank you for making this project better! 🙏
