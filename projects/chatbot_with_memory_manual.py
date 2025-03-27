"""
chatbot_with_memory_manual.py

A basic conversational chatbot with short-term memory using OpenAI's Python SDK directly.
Stores chat history in memory (Python list of dicts).

Concepts: conversational flow, interactive session, short-term memory
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

chat_history = []
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    chat_history.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=chat_history,
    )

    reply = completion.choices[0].message.content
    print("Bot:", reply)

    chat_history.append({"role": "assistant", "content": reply})
