# model.py handles the api request

import os
from dotenv import load_dotenv
from openai import APIError, OpenAI

load_dotenv()  # Load environment variables from .env file


client = OpenAI(
    # Import API key and provider endpoint
    api_key=os.getenv("PROVIDER_API_KEY"),
    base_url=os.getenv("PROVIDER_ENDPOINT"),
)

def get_model_response(messages):
    # Send messages to the model and return its response.
    try:
        response = client.chat.completions.create(
            model=os.getenv("PROVIDER_MODEL"),
            messages=messages,
        )
        return response.choices[0].message.content

    except APIError:
        # Return None to show that the request failed.
        return None