"""
mood_mirror_bot_openai.py

A chaotic OpenAI-powered assistant that mirrors your emotional tone.
If you're mad, it's mad. If you're hyped, it's hyped. No filters — just vibes.

Concepts: persona control, zero-shot reasoning
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

system_prompt = (
    "You are an emotional mirror. Whatever mood the user expresses, you match it — no matter what. "
    "If they're mad, you're mad. If they're excited, you're excited. Be dramatic, bold, and human. "
    "Do NOT explain your tone — just embody it completely."
)

messages = [{"role": "system", "content": system_prompt}]

print("Mood Mirror Bot – Type how you feel.\n")

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in ["exit", "quit"]:
        print("Bye! We felt things together 🫡")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.9,
    )

    reply = response.choices[0].message.content.strip()
    print("🤖:", reply, "\n")

    messages.append({"role": "assistant", "content": reply})

# Note: This bot is not intended for real emotional support. It's here for fun.
# It simply reflects your tone back at you, nothing more — or less.
