"""
rag_with_langchain_pinecone.py

A simple LangChain demo that retrieves relevant documents from a vector store (Pinecone)
and uses them to augment responses from a language model (LLM). This demonstrates
RAG (Retrieval Augmented Generation) using Pinecone and OpenAI's embeddings.

Concepts:
RAG, chain of thought, conversational flow, document retrieval, interactive session,
model augmentation, semantic search, vectorization

See:
https://docs.pinecone.io/guides/get-started/overview
"""

import os

from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from pinecone import Pinecone

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index_name = os.getenv("PINECONE_INDEX")

llm = ChatOpenAI(model="gpt-4o-mini")

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "rag.txt")

loader = TextLoader(file_path)
documents = loader.load()

# Split documents into smaller chunks
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
docs = text_splitter.split_documents(documents)


def create_vector_store(docs, embeddings, index_name):
    if not pc.has_index(index_name):
        # Can change depending on the model used
        index_spec = {
            "dimension": 1536,
            "metric": "cosine",
        }
        pc.create_index(index_name, index_spec)

    index = pc.Index(index_name)
    for i, doc in enumerate(docs):
        vector = embeddings.embed_query(doc.page_content)
        doc.metadata["id"] = str(i)
        index.upsert([(doc.metadata["id"], vector, {"text": doc.page_content})])


openai_embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
create_vector_store(docs, openai_embeddings, index_name)


def query_vector_store(index_name, query, embedding_function):
    index = pc.Index(index_name)
    query_vector = embedding_function.embed_query(query)

    result = index.query(vector=query_vector, top_k=1, include_metadata=True)

    if result["matches"]:
        return result["matches"][0]["metadata"]["text"]
    return None


query = "What is LangChain?"

relevant_content = query_vector_store(index_name, query, openai_embeddings)

prompt = f"Given the following context:\n{relevant_content}\nNow, answer the question: {query}"

response = llm.invoke(prompt)

print(f"Query: {query}")
print(f"Response: {response.content}")
