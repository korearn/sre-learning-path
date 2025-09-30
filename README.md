# 🚀 Python Automation - CI/CD Pipeline

![CI/CD Status](https://github.com/tu-usuario/tu-repo/actions/workflows/ci-cd.yaml/badge.svg)
![Coverage](https://github.com/tu-usuario/tu-repo/raw/main/coverage.svg)

## ✅ Pipeline Features
- **Security**: Safety, Bandit, Semgrep, Trivy
- **Quality**: Black, Flake8, Coverage
- **Testing**: pytest with 85%+ coverage
- **Build**: Docker image
- **Deploy**: Kubernetes validation

## 🛠️ Usage
```bash
# Local development
pip install -r requirements.txt
pytest tests/ -v

# Run security scans
bandit -r ./src
safety check