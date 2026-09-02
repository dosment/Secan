# Sēcan

Sēcan is a small Python AI agent that uses a configurable OpenAI-compatible provider for conversational responses.

## Requirements

- Python 3
- `pip`
- Provider API key

## Setup

From the project directory, create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the required Python packages:

```bash
python -m pip install -r requirements.txt
```

Create a `.env` file in the project directory and add your provider settings:

```text
PROVIDER_ENDPOINT=replace_with_your_provider_url
PROVIDER_API_KEY=replace_with_your_key
PROVIDER_MODEL=replace_with_your_chosen_model
```

Never commit your real API key to Git.

## Usage

Start the agent from the project directory.

```bash
python -m agent_loop.main
```

## Commands

- `/new` starts a new conversation while preserving the system prompt.
- `quit`, `exit`, `/quit`, or `/exit` closes the agent.
