"""
markov_chain_text_generation_with_langchain.py

A simple demo that simulates Markov Chain-like text generation by building each message
on top of the previous one. The idea is to show how the output of one message
becomes the input for the next message, illustrating the core idea of Markov Chains.

Concepts: Markov Chain, chain of thought, conversation history, short-term memory, turn-based dialogue
"""

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

starting_prompt = "Let's generate a conversation that builds step-by-step. Each message should follow the last one."


def run_markov_chain_step(previous_message: str) -> str:
    messages = [HumanMessage(content=previous_message)]

    response = llm.invoke(messages)

    return response.content.strip()


current_message = starting_prompt

print("Starting Markov Chain Text Generation\n")

num_steps = 3
for step in range(num_steps):
    print(f"Step {step + 1}: {current_message}")
    current_message = run_markov_chain_step(current_message)
    print(f"Generated: {current_message}\n")
