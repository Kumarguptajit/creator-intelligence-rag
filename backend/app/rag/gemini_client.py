import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_KEYS = [
    os.getenv("GEMINI_API_KEY_1"),
    os.getenv("GEMINI_API_KEY_2"),
    os.getenv("GEMINI_API_KEY_3"),
]

GEMINI_KEYS = [k for k in GEMINI_KEYS if k]


def generate_content(model, contents):

    last_error = None

    for key in GEMINI_KEYS:

        try:

            client = genai.Client(
                api_key=key
            )

            response = client.models.generate_content(
                model=model,
                contents=contents
            )

            return response

        except Exception as e:

            print(f"Gemini key failed: {e}")
            last_error = e

    raise last_error


def generate_content_stream(model, contents):

    last_error = None

    for key in GEMINI_KEYS:

        try:

            client = genai.Client(
                api_key=key
            )

            return client.models.generate_content_stream(
                model=model,
                contents=contents
            )

        except Exception as e:

            print(f"Gemini key failed: {e}")
            last_error = e

    raise last_error