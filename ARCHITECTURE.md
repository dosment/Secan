# Sēcan Architecture

## Current architecture

```mermaid
flowchart TD
    User[User in terminal] --> Main[agent_loop/main.py]
    Main --> Agent[agent_loop/agent.py]
    Agent --> Commands[agent_loop/commands.py]
    Agent --> Prompts[agent_loop/prompts.py]
    Soul[SOUL.md] --> Prompts
    Agent --> Model[agent_loop/model.py]
    Model --> Provider[OpenAI-compatible provider API]
    Model --> Env[.env]
    Agent --> History[Conversation history]
```

## Current responsibilities

- `main.py` starts the program.
- `agent.py` manages the conversation loop and message history.
- `commands.py` recognizes terminal commands and returns their meaning to `agent.py`.
- `model.py` sends messages to the configured OpenAI-compatible provider and returns the response text.
- `prompts.py` loads `SOUL.md` and combines it with the core instructions to build the system prompt.
- `SOUL.md` describes Sēcan's identity, values, communication style, and boundaries.
- `.env` stores the provider endpoint, model name, and private API key.

## Planned architecture

```mermaid
flowchart TD
    Terminal[Terminal interface] --> Agent[Agent core]
    Telegram[Telegram gateway] -. future .-> Agent
    Agent --> Commands[commands.py]
    Soul[SOUL.md] --> Prompts[Prompt system]
    Agent --> Prompts
    Agent --> Model[Model client]
    Model --> Provider[OpenAI-compatible provider API]
```

The agent core should remain separate from interfaces such as the terminal or Telegram. This allows multiple interfaces to reuse the same conversation and model logic.

At startup, `prompts.py` loads `SOUL.md` and combines it with the core instructions to build `SYSTEM_PROMPT`. The first system message—and every reset through `/new`—uses that combined prompt.
