# LLM Getting Started

A growing collection of practical, beginner-friendly LLM projects using **Python**, **LangChain**, and **LangSmith**.  
Designed to help you learn by building real concepts — from basic prompting to multi-agent coordination.

> Inspired by the [LLM Engineering Cheatsheet](https://github.com/mlane/llm-engineering-cheatsheet)

---

## Quick Start

```bash
git clone https://github.com/mlane/llm-getting-started.git
cd llm-getting-started

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.sample .env
# Fill in your OpenAI / LangSmith API keys

# Run an example project
python3 projects/debate_agent/main.py
```

---

## Python Standards

- **Python version**: 3.11+
- **Formatter**: [`black`](https://github.com/psf/black)
- **Linter**: [`ruff`](https://github.com/astral-sh/ruff)

```bash
# Format code
black .

# Lint code
ruff check .
```

---

## Project Index

| Level           | Project                         | Concepts Practiced                    |
| --------------- | ------------------------------- | ------------------------------------- |
| 🟢 Beginner     | Zero/Few-Shot Prompt Playground | Prompt patterns, zero-shot thinking   |
| 🟢 Beginner     | Simple ChatBot with Memory      | LangChain memory                      |
| 🟡 Intermediate | LLM Agent Debate                | System prompts, disagreement modeling |
| 🟡 Intermediate | Role-Based Support Assistant    | Formatting, role control              |
| 🔴 Advanced     | Retrieval QA from Local Docs    | Vectorstores, retrieval chain         |
| 🔴 Advanced     | Multi-Agent Task Planner (WIP)  | LangGraph, agent chaining             |

---

## Philosophy

This repo is built to be:

- Modular
- Beginner-friendly
- Focused on **thinking**, not just syntax
- Updated as the LLM ecosystem evolves

---

## License

[MIT](./LICENSE)

PRs welcome. Please keep things clean, consistent, and low-dependency.
