# 📚 Harry Potter RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that lets you ask questions about *Harry Potter and the Deathly Hallows* using LangChain, OpenAI, and AstraDB (Cassandra) as the vector store.

---

## 🧠 How It Works

1. The PDF is read and its text is extracted.
2. The text is split into overlapping chunks using LangChain's `RecursiveCharacterTextSplitter`.
3. Each chunk is embedded using OpenAI Embeddings and stored in AstraDB (a managed Cassandra vector database).
4. When you ask a question, the most relevant chunks are retrieved and passed to an OpenAI LLM to generate an answer.

---

## 🗂️ Project Structure
├── app.py               # Main application script
├── harry_potter_7.pdf   # Source PDF (not included in repo)
├── .env                 # Your secret keys — never commit this!
├── .env.example         # Template showing required environment variables
├── .gitignore           # Ensures .env and PDF are not pushed to GitHub
├── requirements.txt     # Python dependencies
└── README.md            # You are here

---

## ⚙️ Prerequisites

- Python 3.8+
- An [OpenAI API key](https://platform.openai.com/api-keys)
- An [AstraDB account](https://astra.datastax.com/) with a Serverless (Vector) database created
- The `harry_potter_7.pdf` file placed in the project root

---

## 🚀 Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Copy the example env file and fill in your credentials:

```bash
cp .env.example .env
```

Open `.env` and replace the placeholder values:
ASTRA_DB_APPLICATION_TOKEN=your_astra_db_token_here
ASTRA_DB_ID=your_astra_db_id_here
OPENAI_API_KEY=your_openai_api_key_here

> ⚠️ **Never commit your `.env` file.** It is listed in `.gitignore` for this reason.

### 4. Add the PDF

Place `harry_potter_7.pdf` in the project root directory. This file is not included in the repository.

### 5. Run the app

```bash
python app.py
```

---

## 💬 Usage

Once running, you'll be prompted to ask questions:
Please type in your first question (or type quit to exit): Who are the Deathly Hallows?
QUESTION: "Who are the Deathly Hallows?"
ANSWER: "The Deathly Hallows are three powerful magical objects..."

Type `quit` at any time to exit.

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `langchain` | Orchestration framework for LLM apps |
| `langchain-community` | Community integrations (AstraDB, etc.) |
| `langchain-openai` | OpenAI LLM and Embeddings |
| `langchain-text-splitters` | Text chunking utilities |
| `cassio` | AstraDB / Cassandra integration |
| `openai` | OpenAI API client |
| `PyPDF2` | PDF text extraction |
| `python-dotenv` | Load environment variables from `.env` |
| `datasets` | Hugging Face dataset support |

Generate a `requirements.txt` with:

```bash
pip freeze > requirements.txt
```

---

## 🔐 Security Notes

- All API keys and tokens are loaded from a `.env` file using `python-dotenv`
- The `.env` file is excluded from version control via `.gitignore`
- If you ever accidentally commit secrets, revoke and regenerate them immediately, then use a tool like [git-filter-repo](https://github.com/newren/git-filter-repo) to purge them from your git history

---

## 🛠️ Potential Improvements

- [ ] Add a web UI (Streamlit or Gradio)
- [ ] Support multiple PDFs / a document directory
- [ ] Add conversation memory for multi-turn dialogue
- [ ] Cache embeddings to avoid re-embedding on every run
- [ ] Add source citation to answers

---

## 📄 License

MIT License — feel free to fork and build on this.