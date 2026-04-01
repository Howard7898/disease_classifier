# GitHub 제출 체크리스트

## ✅ 제출 전 최종 확인사항

### 1. 필수 파일 확인
- [ ] **README.md** - 프로젝트 설명 완료
- [ ] **requirements.txt** - 모든 의존성 포함
- [ ] **LICENSE** - MIT License 포함
- [ ] **.gitignore** - 데이터/결과 파일 제외 설정
- [ ] **train_classifier.py** - 통합 스크립트
- [ ] **scripts/** - 원본 코드 7개 파일

### 2. 문서 파일 (권장)
- [ ] **QUICKSTART.md** - 빠른 시작 가이드
- [ ] **CONTRIBUTING.md** - 기여 가이드
- [ ] **docs/paper.pdf** - 논문 원본
- [ ] **docs/methodology.md** - 방법론 설명 (선택)

### 3. README.md 완성도 확인
- [ ] 프로젝트 제목과 배지
- [ ] 📄 논문 링크 (상단)
- [ ] 📑 Publication 섹션
- [ ] 프로젝트 개요 (한/영)
- [ ] 설치 방법
- [ ] 사용 예제
- [ ] 성능 결과 표
- [ ] Citation 정보
- [ ] 저자 및 연락처

### 4. 코드 품질
- [ ] 모든 스크립트 실행 가능
- [ ] 주석 및 Docstring 작성
- [ ] PEP 8 스타일 준수
- [ ] 에러 처리 포함

### 5. .gitignore 설정
- [ ] `data/` 제외 (IRB 보호)
- [ ] `results/` 제외
- [ ] `*.csv` 제외
- [ ] `venv/` 제외
- [ ] `__pycache__/` 제외

### 6. 보안 및 개인정보
- [ ] 실제 데이터 파일 **절대 업로드 금지**
- [ ] API 키, 비밀번호 등 미포함
- [ ] IRB 승인 정보만 언급 (실제 데이터 X)
- [ ] 개인 이메일/전화번호 확인

### 7. 논문 관련
- [ ] `docs/` 폴더 생성
- [ ] `docs/paper.pdf` 업로드
- [ ] README에 논문 링크 3곳 추가:
  - [ ] 상단 배지
  - [ ] 상단 인용문
  - [ ] Publication 섹션

## 📁 최종 디렉토리 구조

```
health-screening-ml/
├── README.md                    ✅ 필수
├── requirements.txt             ✅ 필수
├── LICENSE                      ✅ 필수
├── .gitignore                   ✅ 필수
├── train_classifier.py          ✅ 필수
├── QUICKSTART.md                👍 권장
├── CONTRIBUTING.md              👍 권장
│
├── scripts/                     ✅ 필수
│   ├── obesity_importance_proj1.py
│   ├── liver_importance_proj1.py
│   ├── highpressure_importance_proj1.py
│   ├── diabete_importance_proj1.py
│   ├── kidney_importance_proj1.py
│   ├── dyslipidemia_importance_proj1.py
│   ├── circul_importance_proj1.py
│   └── obesity_score.py
│
├── docs/                        👍 권장
│   ├── paper.pdf               📑 논문 원본
│   └── methodology.md          
│
└── notebooks/                   💡 선택 (있으면 좋음)
    └── exploratory_analysis.ipynb
```

## 🚫 절대 업로드하지 말 것

```
❌ data/                         # IRB 보호 데이터
❌ results/                      # 실험 결과
❌ *.csv                         # 데이터 파일
❌ venv/                         # 가상환경
❌ __pycache__/                  # Python 캐시
❌ .env                          # 환경변수
```

## 🔄 Git 명령어 순서

```bash
# 1. Git 초기화 (처음만)
git init
git add .
git commit -m "Initial commit: Binary Relevance Health Screening ML"

# 2. GitHub 저장소 연결
git remote add origin https://github.com/yourusername/health-screening-ml.git

# 3. Push
git branch -M main
git push -u origin main

# 4. 논문 파일 추가 (나중에)
mkdir docs
# docs/paper.pdf 파일 복사
git add docs/paper.pdf
git commit -m "Add: Research paper PDF"
git push
```

## 📊 README에 논문 링크하는 3가지 방법

### 1️⃣ 상단 배지 (제일 눈에 띔)
```markdown
[![Paper](https://img.shields.io/badge/Paper-KIIT%202024-red)](docs/paper.pdf)
```

### 2️⃣ 상단 인용문 (Overview 바로 위)
```markdown
> **📄 Research Paper**: [Binary-Relevance-based Multi-Label Classification...](docs/paper.pdf)  
> **Published in**: Journal of KIIT, Vol. 22, No. 2, February 2024
```

### 3️⃣ Publication 섹션 (자세한 정보)
```markdown
## 📑 Publication

### 📥 Access the Paper
- **[Full Paper PDF](docs/paper.pdf)** (Korean)
- **[Journal Website](http://dx.doi.org/10.14801/jkiit.2024.22.2.43)**
```

## ✨ 제출 후 확인사항

### GitHub에서 확인
- [ ] README가 잘 렌더링되는지
- [ ] 논문 PDF 다운로드 되는지
- [ ] 이미지/배지가 잘 보이는지
- [ ] 링크들이 작동하는지

### 코드 테스트
```bash
# 새로운 환경에서 테스트
git clone https://github.com/yourusername/health-screening-ml.git
cd health-screening-ml
pip install -r requirements.txt

# 스크립트 실행 (데이터 있을 경우)
python train_classifier.py --disease obesity
```

## 🎯 심사위원이 보는 포인트

1. **✅ 명확한 문서화**
   - README가 5분 안에 이해되는가?
   - 논문과 코드의 연결이 명확한가?

2. **✅ 재현 가능성**
   - requirements.txt가 완전한가?
   - Random seed가 고정되어 있는가?

3. **✅ 코드 품질**
   - 주석이 충분한가?
   - 구조가 체계적인가?

4. **✅ 연구 윤리**
   - IRB 승인 명시
   - 데이터 보호 철저

5. **✅ 오픈소스 정신**
   - LICENSE 포함
   - CONTRIBUTING 가이드

## 💡 Pro Tips

### 논문 파일 이름
- ✅ 좋음: `paper.pdf`, `KIIT_2024_Teng.pdf`
- ❌ 나쁨: `논문.pdf`, `최종본_수정2_진짜최종.pdf`

### README 작성
- 한국어/영어 병기 (국제 협업 대비)
- 표와 코드 블록 적극 활용
- 성능 수치는 표로 정리

### 커밋 메시지
```bash
# Good
git commit -m "Add: Random Forest classifier for obesity"
git commit -m "Fix: Handle class imbalance in kidney disease"
git commit -m "Docs: Update README with paper link"

# Bad
git commit -m "수정"
git commit -m "final"
git commit -m "asdf"
```

## 📧 문제 발생 시

- **GitHub Issues**: 기술적 문제
- **Email**: mtchoi@skku.edu (연구 관련)
- **Stack Overflow**: 일반적인 Python/ML 질문

---

**모든 항목을 체크한 후 제출하세요!** ✨

마지막 점검일: ________
제출일: ________
