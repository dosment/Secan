# agent.py manages the conversation history

from .model import get_model_response
from .prompts import SYSTEM_PROMPT

def run_agent():
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ]
    while True:   # creates the conversational loop
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        else:
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
