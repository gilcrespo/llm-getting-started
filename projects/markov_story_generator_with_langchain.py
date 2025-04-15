"""
markov_story_generator_with_langchain.py

A LangChain demo that generates a story one sentence at a time, mimicking a Markov Chain-like flow.
Each message builds on the last, showing short-term memory and narrative continuation.

Concepts: Markov Chain, chain of thought, conversation history, short-term memory, turn-based dialogue
"""

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

system_message = SystemMessage(
    content=(
        "You are writing a story one sentence at a time. "
        "Each new sentence should build on what was just written, continuing the plot in a believable and engaging way. "
        "Keep responses short and focused — one sentence per step. Do not summarize the story so far."
    )
)

prompt = ChatPromptTemplate.from_messages(
    [
        system_message,
        MessagesPlaceholder("history"),
        ("human", "{input}"),
    ]
)

history = []
initial_input = "Let's begin a short story about a lonely robot named Echo."

print("Story Generation:\n")

num_steps = 5
for step in range(num_steps):
    chain = prompt | llm
    response = chain.invoke(
        {
            "input": "" if step > 0 else initial_input,
            "history": history,
        }
    )

    reply = response.content.strip()
    print(f"Step {step + 1}: {reply}\n")
    # Note: The full story builds progressively. Each sentence relies on the assistant's last reply.
    history.append(HumanMessage(content=""))
    history.append(AIMessage(content=reply))
