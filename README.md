# AI Study Assistant

AI Study Assistant is a local AI-powered study tool designed to help university students learn from their PDF documents.

The application can analyze PDF documents, generate summaries, create interactive quizzes and flashcards, and answer questions using the content of the selected document.

The project combines document processing, semantic retrieval, local AI models, and a graphical user interface into a single study assistant.

---

## Features

### PDF Summarization

Select a PDF document and generate an AI-powered summary of its content.

The generated summary can also be saved in the results directory.

### Interactive Quiz

Generate multiple-choice questions from the selected PDF.

The quiz system supports:

- Configurable number of questions
- Easy, Medium, and Hard difficulty levels
- Multiple-choice questions
- Immediate answer feedback
- Explanations
- Score calculation
- Accuracy percentage
- Quiz restart

### Study Flashcards

Generate study flashcards from the selected PDF.

The flashcard system supports:

- Question and answer cards
- Answer reveal
- Card-by-card navigation
- Progress tracking
- Review Again functionality

### Chat with Notes

Ask questions about the selected PDF and receive AI-generated answers based on the document.

The chat system supports contextual follow-up questions and document-based retrieval.

### Semantic Retrieval

The application uses semantic embeddings to find document sections that are conceptually related to a user's question.

This allows the assistant to understand questions even when the exact words used by the user do not appear in the document.

### Hybrid Retrieval

Document retrieval combines:

- Semantic similarity
- Keyword relevance

This improves the relevance of retrieved document sections.

### Local AI

The project uses Ollama to run AI models locally.

This allows the main AI processing pipeline to work without sending the document content to a remote AI service.

---

## How It Works

The general workflow is:

PDF
↓
Text Extraction
↓
Text Chunking
↓
Embedding Generation
↓
Semantic + Keyword Retrieval
↓
Relevant Context
↓
Local AI Model
↓
Answer / Summary / Quiz / Flashcards

---

## AI Models

The project currently uses:

- `gemma3:4b` for AI generation
- `nomic-embed-text` for semantic embeddings

Embeddings are compared using cosine similarity.

---

## Technologies

- Python
- CustomTkinter
- Tkinter
- Ollama
- PyMuPDF
- pypdf
- NumPy
- Regular Expressions
- Threading
- Git / GitHub

---

## Project Structure

```text
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
│   ├── ai/
│   │   ├── chat.py
│   │   ├── embeddings.py
│   │   ├── flashcard_parser.py
│   │   ├── quiz_parser.py
│   │   ├── quiz_generator.py
│   │   ├── retriever.py
│   │   └── prompts.py
│   │
│   ├── gui.py
│   ├── main.py
│   └── ...
│
├── DEVLOG.md
├── README.md
└── requirements.txt



```

## Installation
1. Clone the repository
git clone https://github.com/FarazSadeghi323/AI-Study-Assistant.git
cd AI-Study-Assistant

2. Create a virtual environment
python -m venv .venv

3. Activate the virtual environment

Windows PowerShell:
.\.venv\Scripts\Activate.ps1

4. Install dependencies
pip install -r requirements.txt

5. Install Ollama

Install Ollama and make sure it is running on your system.

Then pull the required models:
ollama pull gemma3:4b
ollama pull nomic-embed-text

Running the Application

Start the GUI with:
python src/gui.py

The application will open the AI Study Assistant interface.

Select a PDF and choose one of the available study tools.


## Example Workflow
1.Open the application.
2.Select a PDF document.
3.Generate a summary.
4.Generate an interactive quiz.
5.Review generated flashcards.
6.Ask questions using Chat with Notes.
7.Open the results folder to view generated files.

## Results

Generated outputs are stored in the results/ directory.

The application can generate:
PDF summaries
Quiz files
Flashcard files

Both Markdown and text formats are supported.


Current Status

The project has evolved from a basic PDF processing tool into a local AI-powered study assistant.

Current capabilities include:

PDF processing
AI summarization
Semantic document retrieval
Hybrid retrieval
Context-aware PDF chat
Interactive quizzes
Interactive flashcards
GUI-based study workflow
Local AI inference

Known Limitations

The project is still under active development.

Some GUI state transitions between study modes may require further refinement.

The application is currently primarily designed for desktop environments.

Future Improvements

Potential future improvements include:

Better GUI state management
More responsive layouts
Improved retrieval evaluation
Persistent document indexing
Better conversation memory
More advanced quiz generation
Adaptive quizzes based on previous performance
Spaced-repetition flashcards
Study progress tracking
Document search
Support for additional AI models
Packaging the application as a standalone executable

Development Log

Development decisions, experiments, technical problems, and implemented features are documented in:

DEVLOG.md

The development log contains the evolution of the project from its initial PDF processing functionality to the current AI-powered study assistant.


Author

Faraz Sadeghi

Computer Engineering Student

University of Tehran


License

This project is currently intended as a personal educational and portfolio project.
