
import streamlit as st
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

# ---------------- UI ----------------
st.title("📊 Chatbot for data science and Machine Learning Engineer")

query = st.text_input("Ask a question:")

# ---------------- LOAD DATA ----------------
loader = CSVLoader(file_path="DataScience_QA.csv")
data = loader.load()

# ---------------- SPLIT ----------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
texts = text_splitter.split_documents(data)

# ---------------- EMBEDDINGS ----------------
embeddings = OllamaEmbeddings(
    model="qwen3-embedding:0.6b"   
)

# ---------------- QDRANT ----------------
client = QdrantClient(":memory:")

vector_size = len(embeddings.embed_query("test"))

if not client.collection_exists("test"):
    client.create_collection(
        collection_name="test",
        vectors_config=VectorParams(
            size=vector_size,
            distance=Distance.COSINE
        )
    )

vector_store = QdrantVectorStore(
    client=client,
    collection_name="test",
    embedding=embeddings,
)

# ---------------- ADD DOCUMENTS ----------------
vector_store.add_documents(texts)

# ---------------- RETRIEVER ----------------
retriever = vector_store.as_retriever()

# ---------------- LLM ----------------
llm = OllamaLLM(model="llama3.2:1b")   

# ---------------- QUESTION ----------------
if query:
    docs = retriever.invoke(query)

    context = " ".join([doc.page_content for doc in docs])

    prompt = f"""
    Answer the question based on the context below:

    Context:
    {context}

    Question:
    {query}
    """

    response = llm.invoke(prompt)

    st.subheader("🤖 Answer")
    st.write(response)

    st.subheader("📄 Retrieved Context")
    for doc in docs:
        st.write(doc.page_content)

