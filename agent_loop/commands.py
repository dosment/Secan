# commands.py handles slash commands

def parse_command(user_input):
    user_input = user_input.strip().lower()
    if user_input in ("/exit", "/quit"):
        return "exit"
    elif user_input == ("/new"):
        return "new"
    return None
