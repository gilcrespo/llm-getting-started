"""
chatbot_with_memory.py

A basic conversational chatbot with short-term memory using LangChain.
Remembers previous messages in the current session using ConversationBufferMemory.

Concepts: conversation chaining, interactive session
"""
from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI

load_dotenv()

# Basic example of a chatbot with memory
llm = ChatOpenAI(model="gpt-4o-mini")
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = conversation.predict(input=user_input)
    print("Bot:", response)
