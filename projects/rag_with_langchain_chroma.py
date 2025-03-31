"""
rag_with_langchain_chroma.py

A simple LangChain demo that retrieves relevant documents from a vector store (Chroma)
and uses them to augment responses from a language model (LLM). This demonstrates
RAG (Retrieval Augmented Generation) using Chroma and OpenAI's embeddings.

Concepts:
RAG, chain of thought, conversational flow, document retrieval, interactive session,
model augmentation, semantic search, vectorization

See:
https://docs.trychroma.com/docs/overview/introduction
"""

import os

from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

current_dir = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(current_dir, "db")
file_path = os.path.join(current_dir, "rag.txt")

loader = TextLoader(file_path)
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
docs = text_splitter.split_documents(documents)


def create_vector_store(docs, embeddings, store_name):
    persistent_directory = os.path.join(db_dir, store_name)

    if not os.path.exists(persistent_directory):
        Chroma.from_documents(docs, embeddings, persist_directory=persistent_directory)
    return persistent_directory


openai_embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
create_vector_store(docs, openai_embeddings, "chroma_db_openai")


def query_vector_store(store_name, query, embedding_function):
    persistent_directory = os.path.join(db_dir, store_name)

    if os.path.exists(persistent_directory):
        db = Chroma(
            persist_directory=persistent_directory,
            embedding_function=embedding_function,
        )
        retriever = db.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={"k": 1, "score_threshold": 0.1},
        )
        relevant_docs = retriever.invoke(query)

        if relevant_docs:
            return relevant_docs[0].page_content
    return None


query = "What is LangChain?"

relevant_content = query_vector_store("chroma_db_openai", query, openai_embeddings)

prompt = f"Given the following context:\n{relevant_content}\nNow, answer the question: {query}"
response = llm.invoke(prompt)

print(f"Query: {query}")
print(f"Response: {response.content}")
