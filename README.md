# 🤖 AI Study Assistant

An AI-powered desktop application built with **Python**, **CustomTkinter**, and **local Large Language Models** that helps university students study more efficiently by interacting with PDF documents.

The application can summarize lecture notes, generate quizzes and flashcards, and answer questions based on uploaded PDF documents.

The project uses **local AI models through Ollama**, allowing document analysis and AI-powered interactions without requiring a cloud API key.

The project is being developed publicly as a practical software engineering and AI development project.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![GUI](https://img.shields.io/badge/GUI-CustomTkinter-orange)
![AI](https://img.shields.io/badge/AI-Ollama-purple)
![Version](https://img.shields.io/badge/Version-v0.4.0-blue)

---

## ✨ Features

### 📚 Study Tools

- 📄 **PDF Summarization**
  - Extracts text and information from PDF documents.
  - Processes large documents using text chunking.
  - Generates AI-powered summaries.

- 📝 **AI Quiz Generation**
  - Generates study questions from PDF content.
  - Helps students review lecture material.

- 🗂 **Flashcard Generation**
  - Creates AI-generated flashcards from PDF documents.
  - Supports exporting generated flashcards for later review.

---

## 💬 AI PDF Chat

The application allows users to ask questions about uploaded PDF documents.

### Chat capabilities

- Ask questions about PDF documents.
- Retrieve relevant document sections before generating an answer.
- Uses **semantic search** to find relevant information.
- Uses hybrid **Semantic + Keyword Retrieval**.
- Supports context-aware follow-up questions.
- Maintains conversation history for each PDF.
- Understands references such as:
  - "the second one"
  - "the previous point"
  - "that"
  - "this"
  - "it"
  - "explain that"

### 🧠 Semantic Retrieval

The AI Study Assistant uses embeddings to understand the meaning of questions and document sections.

The system uses:

- `nomic-embed-text`
- 768-dimensional embedding vectors
- Cosine Similarity
- Hybrid Semantic + Keyword Retrieval

This allows the application to retrieve relevant information even when the user's question does not use exactly the same words as the PDF document.

---

## 🧹 Chat Management

- 🗑 Clear chat history.
- ⌨️ `Enter` to send questions.
- 📋 Copy and Paste support.
- ✂️ Cut support.
- `Ctrl + A` to select the complete question.
- Conversation history for each PDF.
- Context-aware follow-up questions.

---

## 🖥 Desktop GUI

- Built with **CustomTkinter**.
- Modern dark interface.
- Custom application icon.
- Improved button styling.
- Dedicated PDF selection and output areas.
- Progress and status indicators.
- Desktop chat interface.

---

## 📤 Export

Generated results can be saved as:

- `.txt`
- `.md`

Supported exports include:

- PDF summaries
- Quizzes
- Flashcards

---

## 🎯 Project Workflow

```text
Select PDF
    ↓
Extract Text
    ↓
Process & Chunk Document
    ↓
AI Analysis
    ↓
┌───────────────────────┐
│ Summary               │
│ Quiz                  │
│ Flashcards            │
│ Chat with Notes       │
└───────────────────────┘

User Question
      ↓
Conversation Context
      ↓
Hybrid Retrieval
(Semantic + Keyword)
      ↓
Relevant PDF Sections
      ↓
Local LLM
      ↓
AI Answer

🛠 Technologies
Python 3.12+
CustomTkinter
PyMuPDF
Pillow
Ollama
Gemma 3
nomic-embed-text
Git
GitHub

🤖 Local AI Models

The project currently uses Ollama to run AI models locally.

Chat and Generation Model
      gemma3:4b

Used for:

Summarization
Quiz generation
Flashcard generation
PDF chat
Embedding Model
      nomic-embed-text

Used for:

Generating semantic embeddings
Document retrieval
Question-to-document similarity comparison

📦 Requirements
Software
Python 3.12+
Ollama
Git
Ollama Models

Install Ollama from the official website and download the required models:

ollama pull gemma3:4b
ollama pull nomic-embed-text

🚀 Installation
1. Clone the repository
git clone https://github.com/FarazSadeghi323/AI-Study-Assistant.git
2. Go to the project directory
cd AI-Study-Assistant
3. Create a virtual environment
python -m venv .venv
4. Activate the virtual environment

Windows PowerShell:

.venv\Scripts\Activate.ps1
5. Install dependencies
pip install -r requirements.txt
6. Install local AI models
ollama pull gemma3:4b
ollama pull nomic-embed-text
7. Verify Ollama models
ollama list
▶️ Run

Start the desktop application with:

python src/gui.py

📁 Project Structure
AI-Study-Assistant/
│
├── assets/
│   └── app_icon.png
│
├── data/
│   └── PDF documents
│
├── results/
│   ├── summary.md
│   ├── summary.txt
│   ├── quiz.md
│   ├── quiz.txt
│   ├── flashcards.md
│   └── flashcards.txt
│
├── src/
│   ├── gui.py
│   ├── main.py
│   ├── pdf_reader.py
│   ├── pdf_processor.py
│   ├── text_processor.py
│   │
│   └── ai/
│       ├── provider.py
│       ├── chat.py
│       ├── embeddings.py
│       ├── retriever.py
│       ├── quiz_generator.py
│       └── flashcard_generator.py
│
├── README.md
├── DEVLOG.md
└── requirements.txt
📈 Development Progress
v0.1.0

Initial stable project milestone.

Desktop GUI
PDF processing
AI summarization
Quiz generation
Flashcard generation
Basic PDF chat
Result export
v0.2.0

Context-aware Chat & GUI Improvements

Context-aware PDF conversations
Per-PDF conversation history
Clear chat functionality
Copy / Paste / Cut support
Enter-to-send
Improved GUI styling
Custom application icon
Improved chat experience
v0.3.0

PDF Retrieval Improvements

Added document retrieval for PDF chat
Retrieved relevant PDF sections before answering questions
Improved answer grounding in document content
Improved PDF question answering accuracy
v0.4.0

Semantic Retrieval & Improved AI Context

Added semantic embeddings using nomic-embed-text
Added cosine similarity for semantic comparison
Added Hybrid Semantic + Keyword Retrieval
Improved document chunking
Added context-aware retrieval queries
Improved follow-up question understanding
Improved chat response context
Improved terminal chat workflow
Added local embedding-based document search
🔮 Future Improvements

Planned improvements include:

Better Quiz generation
Better Flashcard generation
Quiz difficulty levels
Interactive quiz mode
Search inside PDFs
Multi-PDF support
Persistent chat history
Improved AI response quality
Automated testing
Better error handling
Cross-platform packaging
Improved UI/UX
PDF embedding cache
Faster document retrieval

🗺️ Roadmap
[v0.1.0] ──► [v0.2.0] ──► [v0.3.0] ──► [v0.4.0] ──► [v0.5.0] ──► [v1.0.0]

   │              │              │              │              │              │
   │              │              │              │              │              └─ Stable Release
   │              │              │              │              └─ Advanced Study Features
   │              │              │              └─ Semantic Retrieval
   │              │              └─ PDF Retrieval
   │              └─ Context-aware Chat + GUI
   └─ Initial Application

👨‍💻 Author

Faraz Sadeghi

Computer Engineering Student

GitHub:

https://github.com/FarazSadeghi323


📄 License

This project is licensed under the MIT License.

🎓 Project Goal

This project was created to improve practical skills in:

Python development
Software engineering
AI application development
Desktop application development
Retrieval systems
Semantic search
Large Language Models
Local AI models
Git and GitHub

The long-term goal is to turn the project into a more capable AI study platform for university students.

The project is being developed publicly as part of a practical learning journey.
