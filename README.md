# 261020_bucheon_huggingface_bsj

Hugging Face Inference API(fal-ai 제공자)를 이용한 **텍스트 → 비디오 생성기** 데모입니다.
원하는 장면을 문장(프롬프트)으로 입력하면 AI가 비디오를 생성해줍니다.

- 사용 모델: [`Wan-AI/Wan2.2-TI2V-5B`](https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B) (fal-ai 제공자를 통해 호출)
- UI: [Gradio](https://www.gradio.app/)
- 프롬프트는 **영어**로 입력하는 것을 권장합니다 (한국어는 품질이 떨어질 수 있음).

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
VIDEO_MODEL_ID=Wan-AI/Wan2.2-TI2V-5B
```

- `HF_TOKEN`은 필수입니다. 없으면 앱 실행 시 바로 에러가 발생합니다.
- `VIDEO_MODEL_ID`는 선택이며, 생략하면 기본값(`Wan-AI/Wan2.2-TI2V-5B`)이 사용됩니다.
- fal-ai 제공자를 통한 비디오 생성은 호출량에 따라 과금/쿼터 제한이 있을 수 있습니다. 토큰 발급 시 Hugging Face 계정의 Inference Providers 사용 가능 여부를 확인하세요.

> `.env` 파일은 `.gitignore`에 등록되어 있어 깃허브에 올라가지 않습니다. 토큰을 절대 코드에 직접 작성하지 마세요.

## 4. 실행

```bash
python app.py
```

실행 후 터미널에 출력되는 로컬 주소(예: `http://127.0.0.1:7860`)를 브라우저로 열면 됩니다.

## 5. 사용 방법

1. 프롬프트 입력창에 원하는 장면을 영어 문장으로 설명합니다. (예: "A man playing soccer with a dog")
2. "비디오 생성" 버튼을 클릭하면 잠시 후 결과 비디오가 표시됩니다. (비디오 생성은 이미지보다 시간이 오래 걸립니다)
3. 예시 프롬프트를 클릭해 바로 테스트해볼 수도 있습니다.

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
- 다른 비디오 생성 모델로 바꾸고 싶다면 `.env`의 `VIDEO_MODEL_ID` 값을 변경하세요 (단, fal-ai 제공자가 지원하는 모델이어야 합니다).
