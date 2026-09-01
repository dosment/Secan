# AI Agent Harness Project Plan

## Project goal

Build a small, understandable AI agent harness in Python using OpenRouter. The project should be easy to learn from, test, and extend.

## Current state

- [x] Python project organized in the `agent_loop` package.
- [x] OpenRouter connection configured through the `OPENROUTER_API_KEY` environment variable.
- [x] System prompt loaded from `prompts.py`.
- [x] User and assistant messages stored as conversation history.
- [x] Interactive conversation loop supports the `quit` command.
- [x] Friendly error handling for API and connection failures.
- [x] Blank user input is handled with a clear message.
- [x] `main.py` uses a safe entry-point guard.
- [x] Git repository initialized with regular checkpoints.

## Planned milestones

### 1. Stability and usability

- [ ] Choose and document a specific model, or make the model configurable.
- [ ] Improve the quit command and user-facing prompts.
- [ ] Add a `/new` command that resets the conversation while preserving the system prompt.

### 2. Project configuration

- [ ] Add `requirements.txt` with the required packages.
- [ ] Document setup and usage in `README.md`.
- [ ] Add configuration values such as the model name through environment variables.

### 3. Agent identity and prompts

- [ ] Add a `SOUL.md` file describing the agent’s personality, values, tone, and boundaries.
- [ ] Decide how `SOUL.md` should work with the system prompt.

### 4. Testing

- [ ] Add tests for message-history behavior.
- [ ] Add tests for quit and blank-input handling.
- [ ] Test the agent without making real API requests by using a mock response.

### 5. Telegram integration

- [ ] Create a Telegram bot through `@BotFather`.
- [ ] Store the Telegram bot token in `.env`.
- [ ] Reuse the agent’s response logic for Telegram messages.
- [ ] Receive messages with Telegram long polling.
- [ ] Send assistant responses back to the correct Telegram chat.
- [ ] Keep the local terminal interface working.

### 6. Agent capabilities

- [ ] Add a small tool that the agent can call.
- [ ] Define a safe tool-calling structure.
- [ ] Display tool activity clearly to the user.

### 7. Memory and observability

- [ ] Explore short-term conversation memory limits.
- [ ] Add optional conversation logging.
- [ ] Add a simple way to inspect or save conversations.

## Working principles

- Keep the code small and understandable.
- Add one feature at a time.
- Explain new Python concepts before using them.
- Test each meaningful change.
- Use Git checkpoints regularly and review staged files before committing.
- Never store API keys in the repository.

## Immediate next step

Complete the next unchecked task under **Stability and usability**: choose a specific model and document it, or make the model configurable through an environment variable.
