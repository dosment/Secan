# agent.py manages the conversation history

from model import get_model_response
from prompts import SYSTEM_PROMPT

def run_agent():
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ]

    user_input = input("You: ")
    messages.append(
        {
            "role": "user",
            "content": user_input,
        }
    )

    model_response = get_model_response(messages)
    messages.append(
        {
            "role": "assistant",
            "content": model_response,
        }
    )

    print(f"Assistant: {model_response}")
    