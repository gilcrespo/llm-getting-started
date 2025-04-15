"""
weekend_trip_planner_agent.py

A basic OpenAI SDK demo where the model reasons over multiple tools to recommend a city for a weekend trip.
Demonstrates OpenAI's function calling interface with local tool logic and agent-like behavior.

Concepts: chain of thought, system prompts, tool execution
"""

import json
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def get_flight_price(destination: str) -> str:
    prices = {"Chicago": 150, "Miami": 250, "San Diego": 400}
    return json.dumps({"price": prices.get(destination, "unknown")})


def get_food_rating(destination: str) -> str:
    ratings = {
        "Chicago": "9/10 — world-class deep dish and fine dining",
        "Miami": "8/10 — vibrant Latin cuisine",
        "San Diego": "7/10 — great coastal food",
    }
    return json.dumps({"rating": ratings.get(destination, "unknown")})


def get_weather(destination: str) -> str:
    weather = {
        "Chicago": "cold and windy",
        "Miami": "warm and sunny",
        "San Diego": "mild and clear",
    }
    return json.dumps({"weather": weather.get(destination, "unknown")})


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_flight_price",
            "description": "Returns estimated flight cost from New York to the city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "destination": {
                        "type": "string",
                        "description": "The destination city",
                    },
                },
                "required": ["destination"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_food_rating",
            "description": "Returns a food scene rating for a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "destination": {
                        "type": "string",
                        "description": "The destination city",
                    },
                },
                "required": ["destination"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Returns a weather description for the city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "destination": {
                        "type": "string",
                        "description": "The destination city",
                    },
                },
                "required": ["destination"],
            },
        },
    },
]


messages = [
    {
        "role": "system",
        "content": """You are a helpful travel assistant. The user is planning a weekend trip from New York and wants to choose a city based on overall quality.

You have access to tools that provide:
- Weather conditions
- Flight prices
- Food ratings

Use your best judgment to compare a few possible destinations and recommend the best option. Only return your final recommendation — do not explain your reasoning or show tool usage.""",
    },
    {
        "role": "user",
        "content": "Find a warm, affordable city with good food for a weekend trip from New York.",
    },
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools,
    tool_choice="auto",
)

tool_calls = response.choices[0].message.tool_calls
messages.append(response.choices[0].message)

tool_functions = {
    "get_flight_price": get_flight_price,
    "get_food_rating": get_food_rating,
    "get_weather": get_weather,
}

for call in tool_calls:
    name = call.function.name
    args = json.loads(call.function.arguments)
    result = tool_functions[name](**args)

    messages.append(
        {
            "name": name,
            "content": result,
            "role": "tool",
            "tool_call_id": call.id,
        }
    )

final_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
)

print("Weekend trip recommendation:")
print(final_response.choices[0].message.content)
