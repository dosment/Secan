# agent.py manages the conversation history

from .model import get_model_response
from .prompts import SYSTEM_PROMPT
from .commands import parse_command

def run_agent():
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ]
    print("Type /quit or /exit to leave.")
    while True:   # creates the conversational loop
        user_input = input("You: ").strip()
        command = parse_command(user_input)
        if command == "exit":
            print("Goodbye!")
            break
        elif command == "new":
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
