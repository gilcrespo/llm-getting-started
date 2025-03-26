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
agent_1 = SystemMessage(content="You are Agent A. You strongly AGREE with the topic.")
agent_2 = SystemMessage(
    content="You are Agent B. You strongly DISAGREE with the topic."
)
debate_round = [
    agent_1,
    HumanMessage(content=f"Debate this topic: {topic}"),
]

response_a = llm.invoke(debate_round)
print("Agent A:", response_a.content)

debate_round_b = [
    agent_2,
    HumanMessage(content=f"{response_a.content} — respond with your disagreement."),
]

response_b = llm.invoke(debate_round_b)
print("Agent B:", response_b.content)
