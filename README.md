# 🤖 AI Study Assistant

An AI-powered desktop application built with **Python** and **CustomTkinter** that helps university students study more efficiently by interacting with PDF documents.

The application can summarize lecture notes, generate quizzes and flashcards, and answer questions based on uploaded PDF documents using Large Language Models (LLMs).

The project is being developed publicly as a practical software engineering and AI development project.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![GUI](https://img.shields.io/badge/GUI-CustomTkinter-orange)
![Version](https://img.shields.io/badge/Version-v0.2.0-blue)

---

## ✨ Features

### 📚 Study Tools

- 📄 **PDF Summarization**
  - Extracts information from PDF documents.
  - Generates an AI-powered summary.

- 📝 **AI Quiz Generation**
  - Generates study questions from PDF content.
  - Helps students review lecture material.

- 🗂 **Flashcard Generation**
  - Creates AI-generated flashcards from PDF documents.
  - Exports results for later review.

### 💬 AI PDF Chat

- Ask questions about uploaded PDF documents.
- Uses the document summary as the knowledge context.
- Supports **context-aware follow-up questions**.
- Maintains conversation history for each PDF.
- Understands references such as:
  - "the second one"
  - "the previous point"
  - "that"
  - "this"
  - "it"

### 🧹 Chat Management

- 🗑 Clear chat history.
- ⌨️ `Enter` to send questions.
- 📋 Copy and Paste support.
- ✂️ Cut support.
- `Ctrl + A` to select the complete question.

### 🖥 Desktop GUI

- Built with **CustomTkinter**.
- Modern dark interface.
- Custom application icon.
- Improved button styling.
- Dedicated PDF selection and output areas.
- Progress and status indicators.

### 📤 Export

Generated results can be saved and accessed as:

- `.txt`
- `.md`

---

## 🎯 Project Demo

AI Study Assistant provides a simple workflow:

```text
Select PDF
    ↓
Process Document
    ↓
AI Analysis
    ↓
┌───────────────────────┐
│ Summary               │
│ Quiz                  │
│ Flashcards            │
│ Chat with Notes       │
└───────────────────────┘


🛠️ Technologies
Python 3.12+
CustomTkinter
PyMuPDF
OpenAI API
python-dotenv
Git / GitHub


📦 Requirements
Python 3.12+
OpenAI API key
Internet connection for AI-powered features

Main Python dependencies include:

CustomTkinter
PyMuPDF
python-dotenv
OpenAI

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

6. Configure the OpenAI AP
Create a .env file in the project root:
OPENAI_API_KEY=your_api_key_here
Never commit your .env file or expose your API key publicly.

▶️ Run
Start the desktop application with:
python src/gui.py

📁 Project Structure

AI-Study-Assistant/
│
├── assets/
│   └── app_icon.png
│
├── src/
│   ├── gui.py
│   ├── main.py
│   ├── ai/
│   │   ├── chat.py
│   │   ├── provider.py
│   │   └── ...
│   │
│   ├── pdf_reader.py
│   ├── pdf_processor.py
│   └── ...
│
├── results/
│   ├── summary.md
│   ├── summary.txt
│   ├── quiz.md
│   ├── quiz.txt
│   ├── flashcards.md
│   └── flashcards.txt
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
GUI improvements
v0.2.0

Context-aware Chat & GUI Improvements

Context-aware PDF conversations
Per-PDF conversation history
Clear Chat functionality
Copy / Paste / Cut support
Enter-to-send
Improved GUI styling
Custom application icon
Improved chat experience



🔮 Future Improvements

Planned improvements include:

RAG-based document retrieval
Better PDF question answering
Search inside PDFs
Multi-PDF support
More reliable conversation memory
Local LLM support
Improved AI response quality
Automated testing
Better error handling
Cross-platform packaging
Improved UI/UX



🗺️ Roadmap
[v0.1.0] ──► [v0.2.0] ──► [v0.3.0] ──► [v0.4.0] ──► [v1.0.0]

   │              │              │              │              │
   │              │              │              │              └─ Stable Release
   │              │              │              └─ Advanced AI Features
   │              │              └─ Better Retrieval & Testing
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

This project was created to improve my skills in:

Python development
Software engineering
AI application development
Desktop application development
Git and GitHub
Working with Large Language Models
Building practical AI-powered tools

The long-term goal is to turn the project into a more capable AI study platform for university students.

The project is being developed publicly as part of my learning journey.


