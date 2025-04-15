"""
chatbot_with_memory_with_langchain.py

A basic conversational chatbot with short-term memory using LangChain.
Remembers previous messages in the current session using RunnableWithMessageHistory.

Concepts: conversational flow, interactive session, short-term memory
"""

from dotenv import load_dotenv
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

load_dotenv()

history_store = {}
session_id = "demo_session"


def get_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in history_store:
        history_store[session_id] = InMemoryChatMessageHistory()
    return history_store[session_id]


llm = ChatOpenAI(model="gpt-4o-mini")
chain = RunnableWithMessageHistory(llm, get_history)

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye")
        break

    response = chain.invoke(
        input=user_input, config={"configurable": {"session_id": session_id}}
    )

    print("Bot:", response.content)
