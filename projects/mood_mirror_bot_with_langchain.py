"""
mood_mirror_bot_with_langchain.py

A chaotic LangChain-powered assistant that mirrors your emotional tone.
If you're mad, it's mad. If you're hyped, it's hyped. No filters — just vibes.

Concepts: persona control, zero-shot reasoning
"""

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.9)

system_message = SystemMessage(
    content=(
        "You are an emotional mirror. Whatever mood the user expresses, you match it — no matter what. "
        "If they're mad, you're mad. If they're excited, you're excited. Be dramatic, bold, and human. "
        "Do NOT explain your tone — just embody it completely."
    )
)

prompt = ChatPromptTemplate.from_messages(
    [
        system_message,
        ("human", "{input}"),
    ]
)

print("Mood Mirror Bot – Type how you feel.\n")

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in ["exit", "quit"]:
        print("Bye! We felt things together 🫡")
        break

    chain = prompt | llm
    response = chain.invoke({"input": user_input})
    print("🤖:", response.content.strip(), "\n")
    # Note: This bot is not intended for real emotional support. It's here for fun.
    # It simply reflects your tone back at you, nothing more — or less.
