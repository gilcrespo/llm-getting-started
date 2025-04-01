"""
auto_tracing_with_langfuse.py

A simple LangFuse demo that automatically traces input and output using LangFuse's `@observe` decorator.
This demonstrates automatic tracking of function calls to better facilitate model behavior analysis.

Concepts: tool execution

See:
https://langfuse.com/docs/get-started
"""

from dotenv import load_dotenv
from langfuse.decorators import observe
from langfuse.openai import openai

load_dotenv()


@observe()
def pipeline(user_input: str):
    messages = [
        {"role": "user", "content": user_input},
    ]

    response = openai.chat.completions.create(
        messages=messages,
        model="gpt-4o",
    )

    print(f"Response: {response.choices[0].message.content}")


pipeline("Hello, my name is John Doe.")
