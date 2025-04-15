"""
weekend_trip_planner_agent_with_langchain.py

A beginner-friendly LangChain agent that helps users pick a city for a weekend trip from New York.
Demonstrates real agent behavior: reasoning under constraints, comparing options, and choosing actions.

Concepts: tool execution, system prompts, chain of thought
"""

from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()


@tool
def get_flight_price(destination: str) -> str:
    """Returns estimated flight cost from New York to the city."""
    fake_prices = {
        "Chicago": 150,
        "Miami": 250,
        "San Diego": 400,
    }
    return f"${fake_prices.get(destination, 'unknown')}"


@tool
def get_food_rating(destination: str) -> str:
    """Returns a food scene rating for a city."""
    fake_ratings = {
        "Chicago": "9/10 — world-class deep dish and fine dining",
        "Miami": "8/10 — vibrant Latin cuisine",
        "San Diego": "7/10 — great coastal food",
    }
    return fake_ratings.get(destination, "unknown")


@tool
def get_weather(destination: str) -> str:
    """Returns a weather description for the city."""
    fake_weather = {
        "Chicago": "cold and windy",
        "Miami": "warm and sunny",
        "San Diego": "mild and clear",
    }
    return fake_weather.get(destination, "unknown")


tools = [get_flight_price, get_food_rating, get_weather]


system_message = SystemMessage(
    content="""You are a helpful travel assistant. The user is planning a weekend trip from New York and wants to choose a city based on overall quality.

You have access to tools that provide:
- Weather conditions
- Flight prices
- Food ratings

Use your best judgment to compare a few possible destinations and recommend the best option. You may weigh the factors however you think is appropriate. Only return your final recommendation — do not explain your reasoning or show tool usage."""
)

prompt = ChatPromptTemplate.from_messages(
    [
        system_message,
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
agent = create_openai_tools_agent(llm, tools, prompt)
# Set verbose=True to see agent reasoning steps (Thought > Action > Observation)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)


query = "Find a warm, affordable city with good food for a weekend trip from New York."
result = agent_executor.invoke({"input": query})

print("Weekend trip recommendation:", result["output"])
