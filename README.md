# LLM Getting Started

A growing collection of practical, beginner-friendly projects using **Python**, **LangChain**, and **LangSmith** to explore modern LLM patterns.

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
python3 projects/debate_agent.py
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

## Project Roadmap & Learning Path

This repo will grow over time. Projects are grouped by complexity to help you build intuition as LLM concepts evolve from simple to advanced.

✅ = Implemented & ready to run  
💡 = Planned or conceptual for now

| Level           | Project                         | Concepts Practiced                     | Status |
| --------------- | ------------------------------- | -------------------------------------- | ------ |
| 🟢 Beginner     | Simple ChatBot with Memory      | Interactive session, short-term memory | ✅     |
| 🟢 Beginner     | Zero/Few-Shot Prompt Playground | Prompt patterns, zero-shot thinking    | 💡     |
| 🟡 Intermediate | LLM Agent Debate                | System prompts, disagreement modeling  | ✅     |
| 🟡 Intermediate | Role-Based Support Assistant    | Formatting, role control               | 💡     |
| 🔴 Advanced     | Retrieval QA from Local Docs    | Vectorstores, retrieval chain          | 💡     |
| 🔴 Advanced     | Multi-Agent Task Planner        | LangGraph, agent chaining              | 💡     |

---

## Concept Glossary

Each script lists one or more of the following **concepts** it demonstrates:

### LLM Behaviors (Descriptive)

| Behavior                             | Concept                                 |
| ------------------------------------ | --------------------------------------- |
| No examples given                    | zero-shot reasoning                     |
| Examples in prompt                   | few-shot prompting                      |
| Explicit persona or tone             | persona control, system prompts         |
| Responds to previous turns           | conversation history, short-term memory |
| Simulates disagreement or debate     | agent disagreement                      |
| Builds on previous answers           | turn-based dialogue                     |
| Explains steps                       | chain of thought                        |
| Uses external data for context       | RAG (Retrieval Augmented Generation)    |
| Uses retrieved data to augment model | document retrieval, model augmentation  |

### Interaction Patterns

| Structure/Flow                       | Concept                                            |
| ------------------------------------ | -------------------------------------------------- |
| Live user input loop                 | interactive session                                |
| Two or more agents taking turns      | multi-agent interaction                            |
| Message-based prompt passing         | conversational flow                                |
| Uses tools or actions                | tool execution                                     |
| Semantic search for relevant context | document retrieval, semantic search, vectorization |

Use these as a reference when reading or extending scripts.

---

## Philosophy

We believe the best way to learn LLMs is by **doing** — each script is small, focused, and teaches a core idea.

This repo is built to be:

- Modular
- Beginner-friendly
- Focused on **thinking**, not just syntax
- Updated as the LLM ecosystem evolves

---

## License

[MIT](./LICENSE)

PRs welcome. Please keep things clean, consistent, and low-dependency.
