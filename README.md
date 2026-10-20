# 261020_bucheon_huggingface_bsj

Hugging Face Inference API를 이용한 **텍스트 → 이미지 생성기** 데모입니다.
원하는 장면을 문장(프롬프트)으로 입력하면 AI가 이미지를 생성해줍니다.

- 사용 모델: [`black-forest-labs/FLUX.1-schnell`](https://huggingface.co/black-forest-labs/FLUX.1-schnell) (빠르고 무료 등급에서도 사용 가능)
- UI: [Gradio](https://www.gradio.app/)

## 1. 사전 준비

- Python 3.9 이상
- Hugging Face 계정 및 Access Token ([토큰 발급 페이지](https://huggingface.co/settings/tokens)에서 `Read` 권한 토큰 생성)

## 2. 설치

```bash
# 가상환경 생성 (선택)
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # macOS/Linux

# 패키지 설치
pip install -r requirements.txt
```

## 3. 환경변수 설정

`.env.example` 파일을 복사해서 `.env` 파일을 만들고 발급받은 토큰을 입력합니다.

```bash
copy .env.example .env   # Windows
# cp .env.example .env   # macOS/Linux
```

`.env` 내용:

```
HF_TOKEN=hf_xxx_your_huggingface_token_here
MODEL_ID=black-forest-labs/FLUX.1-schnell
```

> `.env` 파일은 `.gitignore`에 등록되어 있어 깃허브에 올라가지 않습니다. 토큰을 절대 코드에 직접 작성하지 마세요.

## 4. 실행

```bash
python app.py
```

실행 후 터미널에 출력되는 로컬 주소(예: `http://127.0.0.1:7860`)를 브라우저로 열면 됩니다.

## 5. 사용 방법

1. 프롬프트 입력창에 원하는 이미지를 문장으로 설명합니다. (예: "눈 내리는 부천역 앞, 따뜻한 조명, 지브리 스타일")
2. 가로/세로 크기를 조절합니다 (기본 768x768).
3. "이미지 생성" 버튼을 클릭하면 몇 초 후 결과 이미지가 표시됩니다.
4. 예시 프롬프트를 클릭해 바로 테스트해볼 수도 있습니다.

## 폴더 구조

```
.
├── app.py              # Gradio 앱 메인 코드
├── requirements.txt    # 필요 라이브러리 목록
├── .env.example         # 환경변수 예시 (실제 토큰은 .env에만 작성)
├── .gitignore
└── README.md
```

## 참고

- Hugging Face Inference API는 모델/계정 등급에 따라 호출 속도 제한이 있을 수 있습니다.
- 다른 이미지 생성 모델로 바꾸고 싶다면 `.env`의 `MODEL_ID` 값을 변경하세요.
