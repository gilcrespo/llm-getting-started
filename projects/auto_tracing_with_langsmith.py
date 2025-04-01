"""
auto_tracing_with_langsmith.py

A simple LangSmith demo that automatically traces input and output using LangSmith's `@traceable` decorator.
This demonstrates automatic tracking of function calls to better facilitate model behavior analysis.

Concepts: tool execution

See:
https://docs.smith.langchain.com/observability#5-trace-openai-calls
"""

import os

from dotenv import load_dotenv
from langsmith import traceable
from langsmith.wrappers import wrap_openai
from openai import OpenAI

load_dotenv()

llm = wrap_openai(
    OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
)


@traceable
def pipeline(user_input: str):
    messages = [
        {"role": "user", "content": user_input},
    ]

    response = llm.chat.completions.create(
        messages=messages,
        model="gpt-4o",
    )

    print(f"Response: {response.choices[0].message.content}")


pipeline("Hello, my name is John Doe.")
