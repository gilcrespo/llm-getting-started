"""
rag_with_langchain_faiss.py

A simple LangChain demo that retrieves relevant documents from a vector store
and uses them to augment responses from a language model (LLM). This demonstrates
RAG (Retrieval Augmented Generation) using FAISS and OpenAI's embeddings.

Concepts:
RAG, chain of thought, conversational flow, document retrieval, interactive session,
model augmentation, semantic search, vectorization

See:
https://faiss.ai/
"""

import logging
import os

import faiss
import numpy as np
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

logging.basicConfig(
    level=logging.INFO, format="%(message)s", handlers=[logging.StreamHandler()]
)

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "rag.txt")

loader = TextLoader(file_path)
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
docs = text_splitter.split_documents(documents)


def create_in_memory_faiss_index(docs, embeddings):
    doc_embeddings = np.array(
        [embeddings.embed_query(doc.page_content) for doc in docs]
    ).astype("float32")

    index = faiss.IndexFlatL2(doc_embeddings.shape[1])
    index.add(doc_embeddings)

    return index, docs


openai_embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
index, docs = create_in_memory_faiss_index(docs, openai_embeddings)


def query_faiss_index(query, index, docs, embeddings):
    query_embedding = embeddings.embed_query(query)
    query_embedding = np.array(query_embedding).astype("float32")
    _, indices = index.search(query_embedding.reshape(1, -1), k=3)

    relevant_docs = [docs[i] for i in indices[0]]
    return relevant_docs


query = "What is LangChain?"

relevant_docs = query_faiss_index(query, index, docs, openai_embeddings)

context = "\n".join([doc.page_content for doc in relevant_docs])
response = llm.invoke(
    f"Given the following context:\n{context}\nNow, answer the question: {query}"
)

print(f"Query: {query}")
print(f"Response: {response.content}")
