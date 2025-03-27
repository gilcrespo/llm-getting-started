"""
debate_agent_manual.py

A basic OpenAI SDK demo where two agents debate a topic using system prompts.
Simulates disagreement and turn-based dialogue using OpenAI's chat API directly.

Concepts: agent disagreement, system prompts, turn-based dialogue
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

topic = "Pineapple belongs on pizza."

agent_a_prompt = "You are Agent A. You strongly AGREE with the topic."
agent_b_prompt = "You are Agent B. You strongly DISAGREE with the topic."


def run_agent(system_prompt: str, user_message: str) -> str:
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message},
    ]
    response = client.chat.completions.create(
        messages=messages,
        model="gpt-4o",
    )
    return response.choices[0].message.content


message_for_a = f"Debate this topic in 2 short sentences: {topic}"
response_a = run_agent(agent_a_prompt, message_for_a)
print("Agent A:", response_a)

message_for_b = f"{response_a} — respond with your disagreement."
response_b = run_agent(agent_b_prompt, message_for_b)
print("Agent B:", response_b)
