# 🚀 GitHub 제출 완벽 가이드

## 단계별 제출 프로세스

### Step 1: 로컬에 프로젝트 폴더 생성

```bash
# 프로젝트 폴더 생성
mkdir health-screening-ml
cd health-screening-ml
```

### Step 2: 필수 파일 복사

다운로드한 파일들을 다음과 같이 배치:

```
health-screening-ml/
├── README.md                    # 다운로드한 파일
├── requirements.txt             # 다운로드한 파일
├── LICENSE                      # 다운로드한 파일
├── .gitignore                   # 다운로드한 파일
├── train_classifier.py          # 다운로드한 파일
├── QUICKSTART.md                # 다운로드한 파일
├── CONTRIBUTING.md              # 다운로드한 파일
└── SUBMISSION_CHECKLIST.md      # 다운로드한 파일
```

### Step 3: 원본 코드 파일 추가

```bash
# scripts 폴더 생성
mkdir scripts

# 업로드한 Python 파일들을 scripts/로 복사
cp /path/to/obesity_importance_proj1.py scripts/
cp /path/to/liver_importance_proj1.py scripts/
cp /path/to/highpressure_importance_proj1.py scripts/
cp /path/to/diabete_importance_proj1.py scripts/
cp /path/to/kidney_importance_proj1.py scripts/
cp /path/to/dyslipidemia_importance_proj1.py scripts/
cp /path/to/circul_importance_proj1.py scripts/
cp /path/to/obesity_score.py scripts/
```

### Step 4: 논문 파일 추가

```bash
# docs 폴더 생성
mkdir docs

# 논문 PDF를 docs/로 복사
cp /path/to/건설-제조_현장_작업자의_복합_질환_선별을_위한_건강_검진_데이터를_사용한_이진-관련성-기반_다중_레이블_분류.pdf docs/paper.pdf
```

**중요**: 파일 이름을 `paper.pdf`로 변경하세요!

### Step 5: Git 초기화

```bash
# Git 초기화
git init

# 파일 추가
git add .

# 첫 커밋
git commit -m "Initial commit: Binary Relevance Multi-Label Health Screening

- Add comprehensive README with paper link
- Include 7 disease classification scripts
- Add unified train_classifier.py
- Include research paper (KIIT 2024)
- Add documentation and contribution guidelines"
```

### Step 6: GitHub 저장소 생성

1. **GitHub.com 접속**
2. **New Repository 클릭**
3. **저장소 설정**:
   - Repository name: `health-screening-ml`
   - Description: `Binary Relevance-based Multi-Label Classification for Occupational Health Screening (KIIT 2024)`
   - Public (추천) 또는 Private
   - **Initialize this repository with**: 체크 해제 (이미 로컬에 있음)
4. **Create repository 클릭**

### Step 7: GitHub에 Push

```bash
# GitHub 저장소 연결
git remote add origin https://github.com/YOUR_USERNAME/health-screening-ml.git

# 브랜치 이름 설정
git branch -M main

# Push
git push -u origin main
```

### Step 8: GitHub에서 최종 확인

1. **README 확인**
   - [ ] 논문 배지 클릭 시 PDF 다운로드?
   - [ ] Publication 섹션 잘 보임?
   - [ ] 표와 코드 블록 정상 렌더링?

2. **파일 확인**
   - [ ] scripts/ 폴더에 8개 파일?
   - [ ] docs/paper.pdf 존재?
   - [ ] .gitignore 작동 (data/ 폴더 안 보임)?

3. **링크 확인**
   - [ ] DOI 링크 작동?
   - [ ] 논문 PDF 다운로드?

## ⚠️ 자주하는 실수

### 1. 데이터 파일 업로드
```bash
# ❌ 절대 하지 마세요!
git add data/health_data_total_proj1.csv  # IRB 위반!

# ✅ .gitignore가 자동으로 제외합니다
```

### 2. 결과 파일 업로드
```bash
# ❌ 불필요한 파일
git add results/  # 자동 생성 파일

# ✅ .gitignore가 자동으로 제외합니다
```

### 3. 가상환경 업로드
```bash
# ❌ 용량만 차지
git add venv/

# ✅ .gitignore가 자동으로 제외합니다
```

### 4. 논문 파일 이름
```bash
# ❌ 한글 이름, 긴 이름
건설-제조_현장_작업자의_복합_질환_선별을_위한_건강_검진_데이터를_사용한_이진-관련성-기반_다중_레이블_분류.pdf

# ✅ 간단하고 명확하게
docs/paper.pdf
```

## 🎨 README에서 논문 보이는 위치

```markdown
# 프로젝트 제목

[배지들...]
[![Paper](https://img.shields.io/badge/Paper-KIIT%202024-red)](docs/paper.pdf)  👈 여기!

> **📄 Research Paper**: [제목](docs/paper.pdf)  👈 여기!
> **Published in**: Journal of KIIT, Vol. 22, No. 2, February 2024

## Overview
...

## Publication  👈 여기 전체 섹션!

### Access the Paper
- [Full Paper PDF](docs/paper.pdf)
- [Journal Website](DOI링크)
```

## 📂 최종 폴더 구조 확인

```bash
# 터미널에서 확인
tree -L 2 -a

# 출력 예상:
health-screening-ml/
├── .git/
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── QUICKSTART.md
├── README.md
├── SUBMISSION_CHECKLIST.md
├── requirements.txt
├── train_classifier.py
├── docs/
│   └── paper.pdf
└── scripts/
    ├── circul_importance_proj1.py
    ├── diabete_importance_proj1.py
    ├── dyslipidemia_importance_proj1.py
    ├── highpressure_importance_proj1.py
    ├── kidney_importance_proj1.py
    ├── liver_importance_proj1.py
    ├── obesity_importance_proj1.py
    └── obesity_score.py
```

## 🔄 수정사항 업데이트

논문 링크나 README 수정 후:

```bash
# 변경사항 확인
git status

# 수정된 파일 추가
git add README.md

# 커밋
git commit -m "Update: Add paper download link to README"

# Push
git push
```

## 🎯 완성 후 할 일

### 1. Repository Settings
- **About** 섹션 설정:
  - Description: "Binary Relevance Multi-Label Classification for Health Screening"
  - Website: DOI 링크
  - Topics: `machine-learning`, `healthcare`, `binary-relevance`, `multi-label-classification`, `occupational-health`

### 2. README Badges 추가
```markdown
![GitHub last commit](https://img.shields.io/github/last-commit/USERNAME/health-screening-ml)
![GitHub repo size](https://img.shields.io/github/repo-size/USERNAME/health-screening-ml)
![GitHub stars](https://img.shields.io/github/stars/USERNAME/health-screening-ml)
```

### 3. Releases (선택)
- Tag: `v1.0.0`
- Release title: "Initial Release - KIIT 2024 Publication"
- Description: 논문 인용 정보

## ✅ 최종 체크리스트

제출 전 마지막 확인:

- [ ] README에 논문 링크 3곳 (배지, 인용문, Publication)
- [ ] docs/paper.pdf 업로드 완료
- [ ] scripts/ 폴더에 8개 Python 파일
- [ ] .gitignore 작동 확인 (data/ 안 보임)
- [ ] requirements.txt 모든 패키지 포함
- [ ] LICENSE 파일 존재
- [ ] GitHub에서 README 정상 렌더링
- [ ] 논문 PDF 다운로드 가능

## 💡 추가 팁

### 저장소 공개 설정
- **Public**: 논문 재현성 ↑, 인용 ↑, 협업 기회 ↑
- **Private**: 초기 개발, 특허 전까지

### README 언어
- 한국어/영어 병기 → 국제 협업 유리
- 주요 내용은 영어 우선
- 세부 설명은 한국어도 OK

### GitHub Pages (선택)
프로젝트 웹사이트로 README 자동 변환
- Settings → Pages → Source: main branch
- 자동 URL: `https://USERNAME.github.io/health-screening-ml/`

---

**문제 발생 시**: GitHub Issues 또는 mtchoi@skku.edu

**행운을 빕니다!** 🍀
