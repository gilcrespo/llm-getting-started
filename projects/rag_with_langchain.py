# rag_with_langchain.py

# A simple LangChain demo that retrieves relevant documents from a vector store
# and uses them to augment responses from a language model (LLM).
# This demonstrates RAG (Retrieval Augmented Generation) using FAISS and OpenAI's embeddings.

# Concepts: document retrieval, model augmentation, vectorization, semantic search, RAG, interactive session, conversational flow, chain of thought

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

if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file {file_path} does not exist.")

loader = TextLoader(file_path)
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# Initialize the embeddings
openai_embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")


# Create an in-memory FAISS index
def create_in_memory_faiss_index(docs, embeddings):
    doc_embeddings = np.array(
        [embeddings.embed_query(doc.page_content) for doc in docs]
    ).astype("float32")

    index = faiss.IndexFlatL2(doc_embeddings.shape[1])  # L2 distance
    index.add(doc_embeddings)

    return index, docs


# Create the FAISS index in-memory
index, docs = create_in_memory_faiss_index(docs, openai_embeddings)


# Function to query the in-memory FAISS index
def query_faiss_index(query, index, docs, embeddings):
    query_embedding = embeddings.embed_query(query)
    query_embedding = np.array(query_embedding).astype("float32")
    _, indices = index.search(query_embedding.reshape(1, -1), k=3)

    relevant_docs = [docs[i] for i in indices[0]]
    return relevant_docs


query = "What is LangChain?"

# Query the FAISS index and retrieve relevant documents
relevant_docs = query_faiss_index(query, index, docs, openai_embeddings)

# Generate a response using the retrieved documents
context = "\n".join([doc.page_content for doc in relevant_docs])
response = llm.invoke(
    f"Given the following context:\n{context}\nNow, answer the question: {query}"
)

print(f"Query: {query}")
print(f"Response: {response.content}")
