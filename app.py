"""
텍스트 -> 이미지 생성기
Hugging Face Inference API(FLUX.1-schnell)를 이용해 프롬프트를 이미지로 변환하는 Gradio 데모.
"""

import os

import gradio as gr
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
MODEL_ID = os.getenv("MODEL_ID", "black-forest-labs/FLUX.1-schnell")

if not HF_TOKEN:
    raise RuntimeError(
        "HF_TOKEN이 설정되지 않았습니다. .env 파일을 만들고 HF_TOKEN=hf_xxx 형태로 입력하세요."
    )

client = InferenceClient(model=MODEL_ID, token=HF_TOKEN)

EXAMPLES = [
    "눈 내리는 부천역 앞, 따뜻한 조명, 지브리 스타일",
    "우주복을 입은 고양이가 달 위에서 커피를 마시는 모습, 디지털 아트",
    "사이버펑크 도시의 야경, 네온사인, 비 오는 거리",
]


def generate_image(prompt: str, width: int, height: int):
    if not prompt or not prompt.strip():
        raise gr.Error("프롬프트를 입력해주세요.")

    image = client.text_to_image(
        prompt,
        width=int(width),
        height=int(height),
    )
    return image


with gr.Blocks(title="텍스트 → 이미지 생성기") as demo:
    gr.Markdown(
        f"""
        # 🎨 텍스트 → 이미지 생성기
        원하는 장면을 문장으로 입력하면 AI가 이미지를 그려줍니다.
        (모델: `{MODEL_ID}`, Hugging Face Inference API 사용)
        """
    )

    with gr.Row():
        with gr.Column(scale=1):
            prompt_input = gr.Textbox(
                label="프롬프트",
                placeholder="예: 비 오는 밤 네온사인이 빛나는 도시 거리",
                lines=3,
            )
            with gr.Row():
                width_input = gr.Slider(256, 1024, value=768, step=64, label="가로(px)")
                height_input = gr.Slider(256, 1024, value=768, step=64, label="세로(px)")
            generate_btn = gr.Button("이미지 생성", variant="primary")
            gr.Examples(examples=EXAMPLES, inputs=prompt_input)
        with gr.Column(scale=1):
            output_image = gr.Image(label="생성된 이미지")

    generate_btn.click(
        fn=generate_image,
        inputs=[prompt_input, width_input, height_input],
        outputs=output_image,
    )
    prompt_input.submit(
        fn=generate_image,
        inputs=[prompt_input, width_input, height_input],
        outputs=output_image,
    )


if __name__ == "__main__":
    demo.launch()
