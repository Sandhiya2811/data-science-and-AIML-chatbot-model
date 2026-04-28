# data-science-and-AIML-chatbot-model

# 📊 Data Science & Machine Learning Chatbot (RAG)

This project is a **Retrieval-Augmented Generation (RAG) chatbot** built using **LangChain, Qdrant, and Ollama**.
It allows users to ask questions based on a CSV dataset and get intelligent answers.

---

## 🚀 Features

* 📂 Load data from CSV file
* ✂️ Split documents into chunks
* 🔍 Convert text into embeddings
* 🧠 Store embeddings in vector database
* 🔎 Retrieve relevant context
* 🤖 Generate answers using LLM
* 🌐 Simple UI using Streamlit

---

## 🛠️ Tech Stack

* Python
* LangChain
* Qdrant (Vector Database)
* Ollama (Local LLM & Embeddings)
* Streamlit (Frontend UI)

---

## 📁 Project Structure

```
project_1/
│
├── ds_chatbot.py          # Main Streamlit app
├── DataScience_QA.csv     # Dataset
└── README.md              # Documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv .venv
```

Activate:

**Windows:**

```bash
.venv\Scripts\activate
```

**Mac/Linux:**

```bash
source .venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit langchain langchain-community langchain-qdrant qdrant-client langchain-ollama
```

---

## 🤖 Setup Ollama Models

Install **Ollama** and download required models:

```bash
ollama pull llama3.2:1b
ollama pull qwen3-embedding:0.6b
```

---

## ▶️ Run the Application

```bash
streamlit run ds_chatbot.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🧠 How It Works

1. Load CSV data
2. Split into smaller chunks
3. Convert chunks → embeddings
4. Store in Qdrant vector database
5. User asks question
6. Retrieve relevant chunks
7. Send context + question to LLM
8. Generate final answer

👉 This approach is called **RAG (Retrieval-Augmented Generation)**

---

## 💡 Example Usage

**Input:**

```
What is machine learning?
```

**Output:**

```
Machine learning is a subset of AI that enables systems to learn from data...
```

---

## ⚠️ Notes

* Ensure CSV file is in correct path
* Make sure Ollama is running:

```bash
ollama serve
```

* First run may take time (model loading)

---

## 📌 Future Improvements

* 📤 Upload CSV dynamically
* 💬 Chat history (memory)
* 🎨 Better UI design
* ☁️ Deploy on cloud

---

## 👩‍💻 Author

**Sandhiya**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
