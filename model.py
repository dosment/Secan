# model.py handles the api request

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Load environment variables from .env file

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

def get_model_response(messages):
    """Send messages to the model and return its response."""
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
    )
    return response.choices[0].message.content
