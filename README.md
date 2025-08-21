# 🛠️ RepairBot

RepairBot is an **AI-powered assistant** that helps with **car repair and troubleshooting**.  
It reads car repair manuals (PDFs), understands them, and answers your questions using the power of **LangChain**, **Hugging Face embeddings**, and **Groq LLMs**.  

Built with **Streamlit** for an easy-to-use interface. 🚀  

---

## 📌 Features
- 📂 Load and process repair manuals (PDFs)  
- ✂️ Smart text chunking for better context  
- 🔎 Semantic search using Hugging Face embeddings  
- ⚡ Fast and accurate answers powered by Groq LLM  
- 🎨 Simple, user-friendly Streamlit interface  

---

1. **Document Loading**

   * Loads repair manuals with `LangChain PyPDFLoader`.

2. **Text Chunking**

   * Splits text into smaller chunks using `LangChain TextSplitter`.

3. **Embeddings**

   * Uses Hugging Face model:
     `sentence-transformers/all-MiniLM-L6-v2`
   * Enables semantic search to find the most relevant chunks.

4. **Language Model (LLM)**

   * Uses **Groq (ChatGroq)** with a free API key for fast and contextual answers.

5. **User Interface**

   * **Streamlit app** where users can ask repair questions interactively.

---

## 🛠️ Tech Stack

* [LangChain](https://www.langchain.com/) – framework for LLM apps
* [PyPDFLoader](https://python.langchain.com/docs/modules/data_connection/document_loaders/pdf) – load PDF manuals
* [TextSplitter](https://python.langchain.com/docs/modules/data_connection/document_transformers/text_splitter) – split large text into chunks
* [Hugging Face Embeddings](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) – semantic embeddings model
* [Groq LLM (ChatGroq)](https://groq.com/) – large language model backend
* [Streamlit](https://streamlit.io/) – web UI

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/haiderfarooq7/repairbot.git
cd repairbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your API key

Create a `.env` file in the project folder:

```
GROQ_API_KEY=your_api_key_here
```

### 4. Run the app

```bash
streamlit run repairbot.py
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Open a pull request or start a discussion to improve RepairBot.

---

## 📄 License

This project is licensed under the **MIT License**.

```

