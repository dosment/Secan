# prompts.py stores the agent's behavior instructions

from pathlib import Path

SOUL_PATH = Path(__file__).resolve().parent.parent / "SOUL.md"
SOUL_TEXT = SOUL_PATH.read_text(encoding="utf-8")

CORE_PROMPT = """
You are a helpful assistant. Answer clearly and briefly.
"""
SYSTEM_PROMPT = f'{CORE_PROMPT.strip()}\n\n{SOUL_TEXT.strip()}'
