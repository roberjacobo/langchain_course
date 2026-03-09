# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

LangChain Udemy course project — a learning repo exploring LLM integrations (Ollama, Anthropic, Google GenAI) with LangChain and Streamlit.

## Commands

```bash
# Install dependencies (uses uv package manager)
uv sync

# Run scripts
python src/hello_world.py
python src/hello_world_advanced.py

# Run Streamlit chatbot
streamlit run src/tema_1/streamlit_chatbot.py
```

Requires a local Ollama instance running with the `gemma3:27b` model.

## Architecture

- `src/` — Course exercises organized by topic (`tema_1/`, etc.)
- `docs/notes.md` — Learning notes with key takeaways per topic
- `main.py` — Entry point (minimal)

### Key Patterns

- **ChatOllama** for local LLM inference via Ollama
- **LCEL** (pipe `|` operator) to compose chains: `prompt | llm | parser`
- **PromptTemplate** with `{placeholders}` (not f-strings) for dynamic prompts
- **Streamlit** with `st.session_state` for persistent chat history across reruns

### LLM Providers

Three providers are configured: `langchain-ollama` (local), `langchain-anthropic`, `langchain-google-genai`. API keys are stored in `.env`.

## Conventions

- Code comments are written in **Spanish** (learning context)
- Python 3.12+ required
- Dependencies managed with **uv** (lock file: `uv.lock`)
