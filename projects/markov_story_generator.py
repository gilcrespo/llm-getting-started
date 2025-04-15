"""
markov_story_generator.py

A step-by-step story generator that builds one sentence at a time,
mimicking a Markov Chain-like process. Each new step builds upon the
previous, demonstrating short-term memory and incremental narrative flow.

Concepts: Markov Chain, chain of thought, conversation history, short-term memory, turn-based dialogue
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

llm = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

system_prompt = (
    "You are writing a story one sentence at a time. Each new sentence should build "
    "on what was just written, continuing the plot in a believable and engaging way. "
    "Keep responses short and focused — one sentence per step. Do not summarize the story so far."
)

messages = [
    {"role": "system", "content": system_prompt},
    {
        "role": "user",
        "content": "Let's begin a short story about a lonely robot named Echo.",
    },
]

print("Story Generation:\n")

num_steps = 5
for step in range(num_steps):
    response = llm.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
    )

    reply = response.choices[0].message.content.strip()
    print(f"Step {step + 1}: {reply}\n")
    # Note: The full story builds progressively. Each sentence relies on the assistant's last reply.
    messages.append({"role": "assistant", "content": reply})
