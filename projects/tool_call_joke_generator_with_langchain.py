"""
tool_call_joke_generator_with_langchain.py

A simple LangChain demo where the model uses a registered tool to fetch a random programming joke.
Illustrates OpenAI-style tool execution with structured input and callable output.

Concepts: tool execution
"""

import requests
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")


@tool
def get_random_programming_joke() -> str:
    """Returns a random programming joke."""
    response = requests.get(
        "https://official-joke-api.appspot.com/jokes/programming/random"
    )
    joke = response.json()[0]
    return f"{joke['setup']} — {joke['punchline']}"


llm_with_tool = llm.bind_tools([get_random_programming_joke])

prompt = HumanMessage(content="Tell me a programming joke.")
tool_calls = llm_with_tool.invoke([prompt]).tool_calls

# Tool takes no parameters, so we must still pass an empty dict (`{}`) to invoke it manually
joke = get_random_programming_joke.invoke({})
print("Response:", joke)
