import os
import itertools
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_KEYS = [
    os.getenv("GEMINI_API_KEY_1"),
    os.getenv("GEMINI_API_KEY_2"),
    os.getenv("GEMINI_API_KEY_3"),
]

GEMINI_KEYS = [k for k in GEMINI_KEYS if k]

CLIENTS = [
    genai.Client(api_key=key)
    for key in GEMINI_KEYS
]

client_cycle = itertools.cycle(CLIENTS)

def generate_content(model, contents):

    last_error = None

    for _ in range(len(CLIENTS)):

        client = next(client_cycle)

        try:

            return client.models.generate_content(
                model=model,
                contents=contents
            )

        except Exception as e:

            print(f"Gemini key failed: {e}")
            last_error = e

    raise last_error

def generate_content_stream(model, contents):

    last_error = None

    for _ in range(len(CLIENTS)):

        client = next(client_cycle)

        try:

            stream = client.models.generate_content_stream(
                model=model,
                contents=contents
            )

            return stream

        except Exception as e:

            print(f"Gemini key failed: {e}")
            last_error = e

    raise last_error

