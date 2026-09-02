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
    print("Type quit, exit, /quit, or /exit to leave.")
    while True:   # creates the conversational loop
        user_input = input("You: ").strip()
        if user_input.lower() in ("quit", "exit", "/exit", "/quit"):
            print("Goodbye!")
            break
        elif user_input.lower() == "/new":
            messages = [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                }
            ]
            print("Started a new conversation.")
        elif not user_input:
            print("Please enter a message.")
            continue
        else:
            messages.append(
                {
                    "role": "user",
                    "content": user_input,
                }
            )
            model_response = get_model_response(messages)

            if model_response is None:
                print("Assistant: Sorry, I couldn't reach the model. Please try again.")
                continue
            
            messages.append(
                {
                    "role": "assistant",
                    "content": model_response,
                }
            )
            print(f"Assistant: {model_response}")
