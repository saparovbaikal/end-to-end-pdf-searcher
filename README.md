# End-to-End PDF Searcher (AI generated README)

A Retrieval-Augmented Generation (RAG) system that allows users to ask questions about PDF documents and receive context-based answers using Google's Gemini API.

The project implements an end-to-end pipeline for extracting, processing, embedding, and retrieving information from PDF documents.

## Features

- **PDF Text Extraction:** Extracts and cleans text from PDF documents using `pdfplumber`.
- **Text Chunking:** Splits extracted text into overlapping chunks using LangChain's `RecursiveCharacterTextSplitter`.
- **Text Embeddings:** Generates vector embeddings using `sentence-transformers/all-MiniLM-L6-v2`.
- **Vector Storage:** Stores document embeddings and performs similarity search using ChromaDB.
- **Context-Aware Generation:** Uses Google Gemini API to generate answers based on retrieved document content.
- **Source Metadata:** Preserves document source information in text chunks.

## Architecture

The application follows a RAG pipeline:

```text
       PDF Document
             |
             v
      Text Extraction
         (pdfplumber)
             |
             v
        Text Cleaning
             |
             v
        Text Chunking
      (500 chars, 50 overlap)
             |
             v
       Text Embeddings
    (all-MiniLM-L6-v2)
             |
             v
        ChromaDB
             |
             |
User Question  |
      |        |
      v        |
 Query Embedding
      |
      v
 Similarity Search
      |
      v
 Top 5 Relevant Chunks
      |
      v
   Gemini API
      |
      v
  Generated Answer
```

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| pdfplumber | PDF text extraction |
| LangChain | Text splitting and document processing |
| Sentence Transformers | Text embeddings |
| ChromaDB | Vector database |
| Google Gemini API | Answer generation |

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/saparovbaikal/end-to-end-pdf-searcher.git
cd end-to-end-pdf-searcher
```

### 2. Install dependencies

```bash
pip install pdfplumber
pip install langchain-text-splitters
pip install langchain-huggingface
pip install langchain-chroma
pip install sentence-transformers
pip install google-genai
```

### 3. Configure Gemini API

Obtain an API key from [Google AI Studio](https://aistudio.google.com/apikey).

Set the environment variable:

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="your_api_key"
```

**Linux / macOS:**
```bash
export GEMINI_API_KEY="your_api_key"
```

## Usage

Place your PDF document in the project directory.

The current example uses `algorithms_book.pdf`.

Run the application:

```bash
python main.py
```

The application will:

1. Extract text from the PDF.
2. Split the text into chunks.
3. Generate embeddings and store them in ChromaDB.
4. Retrieve the 5 most relevant chunks for the predefined question.
5. Send the retrieved context and question to Gemini.
6. Print the generated answer.

To change the document or question, modify the corresponding arguments in `main.py`.

## Project Structure

```text
end-to-end-pdf-searcher/
│
├── algorithms_book.pdf
├── main.py
├── extracting_text.py
├── chunking.py
├── loading_data.py
├── vector_store.py
├── getting_answer.py
│
├── models/       # Embedding model cache
└── vector_db/    # Persistent ChromaDB storage
```

## Limitations

- Currently supports text extraction from PDFs; OCR for scanned documents is not implemented.
- The application uses a predefined PDF path and question in `main.py`.
- Answer generation requires a valid Gemini API key.
- Retrieval quality depends on document content, chunking, and embedding similarity.

## Project Status

Experimental project developed to explore RAG architecture, semantic search, vector databases, embeddings, and LLM integration.
