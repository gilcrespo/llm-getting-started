"""
tool_call_joke_generator.py

A basic OpenAI SDK demo where the model uses function calling to retrieve a random programming joke.
Demonstrates OpenAI's tool (function) calling interface with a local API integration.

Concepts: tool execution
"""

import json
import os

import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def get_random_programming_joke() -> str:
    """Returns a random programming joke."""
    response = requests.get(
        "https://official-joke-api.appspot.com/jokes/programming/random"
    )
    joke = response.json()[0]
    return json.dumps({"joke": f"{joke['setup']} — {joke['punchline']}"})


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_random_programming_joke",
            "description": "Fetches a random programming joke from the internet.",
            "parameters": {
                "type": "object",
                "properties": {},  # No inputs needed
            },
        },
    }
]

messages = [
    {
        "role": "user",
        "content": "Tell me a programming joke.",
    }
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools,
    tool_choice="auto",  # Let model decide
)

response_message = response.choices[0].message
tool_calls = response_message.tool_calls

if tool_calls:
    tool_call = tool_calls[0]
    function_response = get_random_programming_joke()

    messages.append(response_message)
    messages.append(
        {
            "tool_call_id": tool_call.id,
            "role": "tool",
            "name": tool_call.function.name,
            "content": function_response,
        }
    )

    final_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
    )

    print("Response:")
    print(final_response.choices[0].message.content)
else:
    print("No tool call was triggered.")
