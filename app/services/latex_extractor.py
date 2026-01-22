import base64
import requests
import re
from app.config import OPENAI_API_KEY

OPENAI_ENDPOINT = "https://api.openai.com/v1/responses"
MODEL_NAME = "gpt-4.1-mini"

SYSTEM_PROMPT = (
    "You are a mathematical OCR engine. "
    "Extract ONLY mathematical expressions from the image "
    "and convert them into VALID LaTeX. "
    "Do NOT explain anything. "
    "Do NOT include normal text. "
    "Output ONLY LaTeX."
)


def extract_latex_from_image(image):
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is missing")

    image_base64 = image_to_base64(image)
    image_data_url = f"data:image/png;base64,{image_base64}"

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL_NAME,
        "input": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": SYSTEM_PROMPT
                    },
                    {
                        "type": "input_image",
                        "image_url": image_data_url
                    }
                ]
            }
        ],
        "temperature": 0
    }

    response = requests.post(
        OPENAI_ENDPOINT,
        headers=headers,
        json=payload,
        timeout=60
    )

    if response.status_code != 200:
        raise ValueError(
            f"OCR model failed: {response.status_code} - {response.text}"
        )

    data = response.json()

    latex = extract_text_from_response(data)

    if not latex:
        raise ValueError("No LaTeX output detected")

    return clean_latex(latex)


def extract_text_from_response(data: dict) -> str:
    """
    Safely extracts text from OpenAI Responses API output
    """
    for item in data.get("output", []):
        if item.get("type") == "message":
            for content in item.get("content", []):
                if content.get("type") == "output_text":
                    return content.get("text", "")
    return ""


def clean_latex(text: str) -> str:
    """
    Removes markdown code fences and trims LaTeX
    """
    # Remove ```latex and ``` fences
    text = re.sub(r"```latex", "", text, flags=re.IGNORECASE)
    text = re.sub(r"```", "", text)

    # Trim whitespace
    return text.strip()


def image_to_base64(image):
    import io
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()
