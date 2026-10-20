"""
텍스트 -> 비디오 생성기
Hugging Face Inference API(fal-ai, Wan2.2-TI2V-5B)를 이용해 프롬프트를 비디오로 변환하는 Gradio 데모.
"""

import os
import tempfile

import gradio as gr
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
MODEL_ID = os.getenv("VIDEO_MODEL_ID", "Wan-AI/Wan2.2-TI2V-5B")

if not HF_TOKEN:
    raise RuntimeError(
        "HF_TOKEN이 설정되지 않았습니다. .env 파일을 만들고 HF_TOKEN=hf_xxx 형태로 입력하세요."
    )

client = InferenceClient(
    provider="fal-ai",
    api_key=HF_TOKEN,
)

EXAMPLES = [
    "A man playing soccer with a dog",
    "A young man walking on the street",
    "A cat wearing a spacesuit drinking coffee on the moon",
]


def generate_video(prompt: str):
    if not prompt or not prompt.strip():
        raise gr.Error("프롬프트를 입력해주세요.")

    video_bytes = client.text_to_video(prompt, model=MODEL_ID)

    with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as tmp_file:
        tmp_file.write(video_bytes)
    return tmp_file.name


with gr.Blocks(title="텍스트 → 비디오 생성기") as demo:
    gr.Markdown(
        f"""
        # 🎬 텍스트 → 비디오 생성기
        원하는 장면을 영어 문장으로 입력하면 AI가 비디오를 만들어줍니다.
        (모델: `{MODEL_ID}`, Hugging Face Inference API / fal-ai 사용)
        """
    )

    with gr.Row():
        with gr.Column(scale=1):
            prompt_input = gr.Textbox(
                label="프롬프트 (영어 권장)",
                placeholder="예: A man playing soccer with a dog",
                lines=3,
            )
            generate_btn = gr.Button("비디오 생성", variant="primary")
            gr.Examples(examples=EXAMPLES, inputs=prompt_input)
        with gr.Column(scale=1):
            output_video = gr.Video(label="생성된 비디오")

    generate_btn.click(
        fn=generate_video,
        inputs=prompt_input,
        outputs=output_video,
    )
    prompt_input.submit(
        fn=generate_video,
        inputs=prompt_input,
        outputs=output_video,
    )


if __name__ == "__main__":
    demo.launch()
