"""
debate_agent.py

A simple LangChain demo where two agents debate a topic using different system prompts.
Simulates disagreement and turn-based dialogue using ChatOpenAI and message history.

Concepts: agent disagreement, system prompts, turn-based dialogue
"""

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")
topic = "Pineapple belongs on pizza."
agent_a = SystemMessage(content="You are Agent A. You strongly AGREE with the topic.")
agent_b = SystemMessage(
    content="You are Agent B. You strongly DISAGREE with the topic."
)


def run_agent(agent_system_message: SystemMessage, message: str) -> str:
    messages = [agent_system_message, HumanMessage(content=message)]
    response = llm.invoke(messages)
    return response.content


message_for_a = f"Debate this topic in 2 short sentences: {topic}"
response_a = run_agent(agent_a, message_for_a)
print("Agent A:", response_a)

message_for_b = f"{response_a} — respond with your disagreement."
response_b = run_agent(agent_b, message_for_b)
print("Agent B:", response_b)
