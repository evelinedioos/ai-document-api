# AI Document Assistant

An AI-powered document assistant that analyzes PDFs. Upload a document, get an automatic summary, and ask questions about the content — powered by a RAG pipeline built with FastAPI, OpenAI, and cosine similarity search.

---

## What it does

1. **Upload a PDF** → the app extracts the text and splits it into chunks
2. **Automatic summary** → OpenAI generates a concise summary of the document
3. **Ask questions** → the app finds the most relevant chunks using semantic search and answers your question using GPT

---

## Architecture

```
PDF Upload
    │
    ▼
Text Extraction (pypdf)
    │
    ▼
Chunking (paragraph/sentence-aware)
    │
    ▼
Embeddings (OpenAI text-embedding-3-small)
    │
    ▼
Document Store (in-memory)
    │
    ├──────────────────────────┐
    ▼                          ▼
Summary (GPT-4.1-mini)     Question Answering
                                │
                                ▼
                         Question Embedding
                                │
                                ▼
                         Cosine Similarity Search
                                │
                                ▼
                         Top 3 Relevant Chunks
                                │
                                ▼
                         GPT-4.1-mini → Answer
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| AI Model | GPT-4.1-mini (OpenAI) |
| Embeddings | text-embedding-3-small (OpenAI) |
| PDF Processing | pypdf |
| Similarity Search | Cosine similarity (custom implementation) |
| Language | Python 3.11+ |

---

## Project Structure

```
ai-document-api/
├── app/
│   └── main.py               # FastAPI app entry point
├── routes/
│   ├── upload.py             # POST /upload
│   ├── summarize.py          # POST /summarize
│   └── question_routes.py    # POST /ask/{document_id}
├── services/
│   ├── pdf_service.py        # PDF text extraction
│   ├── summarize_service.py  # Summary logic
│   ├── question_service.py   # Question answering logic
│   ├── openai_service.py     # OpenAI API calls
│   ├── chunking_service.py   # Text chunking with overlap
│   └── similarity_service.py # Cosine similarity + retrieval
├── data/
│   └── document_store.py     # In-memory document storage
├── utils/
│   └── config.py             # Environment variables
├── .env                      # API keys (not committed)
├── requirements.txt
└── README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/evelinedioos/ai-document-api.git
cd ai-document-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root of the project:

```
OPENAI_API_KEY=your_openai_api_key_here
APP_NAME=AI Document API
DEBUG=False
```

### 5. Run the server

```bash
uvicorn app.main:app --reload
```

The API is now running at `http://localhost:8000`

---

## API Usage

### Interactive docs

Go to `http://localhost:8000/docs` for the automatic Swagger UI — you can test all endpoints directly in your browser.

### Endpoints

#### Upload a PDF
```
POST /upload
Content-Type: multipart/form-data

file: your_document.pdf
```

Response:
```json
{
  "document_id": "abc-123",
  "filename": "paper.pdf",
  "page_count": 5,
  "character_count": 12400,
  "chunk_count": 14,
  "summary": "This document discusses..."
}
```

#### Ask a question
```
POST /ask/{document_id}
Content-Type: application/x-www-form-urlencoded

question: What are the main conclusions?
```

Response:
```json
{
  "document_id": "abc-123",
  "question": "What are the main conclusions?",
  "answer": "The document concludes that...",
  "sources_used": 3,
  "similarities": [0.91, 0.75, 0.62]
}
```

#### Summarize text directly
```
POST /summarize
Content-Type: application/json

{ "text": "Your text here..." }
```

---

## How RAG works in this project

RAG stands for **Retrieval Augmented Generation**. Instead of sending the entire document to GPT (which is expensive and hits token limits), this app:

1. Splits the document into small chunks
2. Converts each chunk into a vector (embedding) that represents its meaning
3. When you ask a question, converts the question into a vector too
4. Finds the chunks most similar to your question using cosine similarity
5. Sends only those relevant chunks to GPT — not the whole document

This makes the system faster, cheaper, and more accurate.

---

## What I learned building this

- FastAPI — building REST APIs with automatic documentation
- Service architecture — separating routes, services, and data layers
- PDF processing — extracting and cleaning text from PDFs
- OpenAI API — chat completions and embeddings
- RAG pipeline — chunking, embedding, retrieval, and generation
- Git & GitHub — version control and project management
- Error handling — HTTP exceptions and try/except patterns

---

## Next steps

- [ ] Persistent storage (PostgreSQL)
- [ ] Docker support
- [ ] Frontend UI
- [ ] Authentication
- [ ] Deployment (Railway / Render)

