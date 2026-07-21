# AI Study Assistant - Development Log

## Day 1

### Features
- Created the initial project structure.
- Initialized a local Git repository.
- Created the GitHub repository.
- Connected the local project to GitHub.

### What I Learned
- How Git repositories are initialized.
- Basic GitHub workflow.
- Why version control is essential for software development.

---

## Day 2

### Features
- Set up a Python virtual environment.
- Installed project dependencies.
- Installed python-dotenv.
- Created the first executable version of the application.

### What I Learned
- How Python virtual environments isolate project dependencies.
- Why dependency management is important.
- How to organize a Python project from the beginning.

---

## Day 3

### Features
- Added an interactive terminal menu.
- Implemented the main application loop.
- Learned the complete Git workflow.
- Pushed the first functional version to GitHub.

### What I Learned
- How to build interactive console applications.
- Git commands: status, add, commit and push.
- The importance of committing changes frequently.

---

## Day 4

### Features
- Created pdf_reader.py.
- Installed the pypdf library.
- Implemented PDF page counting.
- Successfully read the first PDF document.

### What I Learned
- How Python modules work.
- Basic PDF processing.
- Separating functionality into reusable modules.

---

## Day 5

### Features
- Tested multiple PDF files.
- Investigated compatibility issues.
- Compared different PDF libraries.
- Started evaluating PyMuPDF as an alternative.

### What I Learned
- Not all PDF files follow the same internal structure.
- Testing with different files is essential.
- Debugging starts with identifying the real problem.

---

## Day 6

### Features
- Migrated from pypdf to PyMuPDF.
- Implemented PDF text extraction.
- Improved PDF compatibility.

### What I Learned
- Different libraries have different strengths.
- Debugging is about finding the real cause.
- Choosing the right tool is part of software engineering.

---

## Day 7

### Features
- Replaced pypdf with PyMuPDF.
- Successfully extracted text from valid PDF files.
- Added support for user-defined PDF paths.

### What I Learned
- Always verify the input before changing the code.
- Different PDF libraries have different compatibility.
- Debugging means finding the root cause, not guessing.

---

## Day 8

### Features
- Improved project structure.
- Refactored PDF-related functions.
- Simplified the application workflow.
- Prepared the project for AI integration.

### What I Learned
- Clean code improves readability.
- Small refactoring makes future development easier.
- Building software is an iterative process.

---

## Day 9

### Features
- Added a PDF file picker using Tkinter.
- Added error handling for invalid PDF files.
- Improved application structure by separating functions.
- Successfully tested PDF text extraction with valid PDF files.

### What I Learned
- How to use Tkinter file dialogs.
- How to handle exceptions using try/except.
- The importance of testing with valid input data.
- How to debug file-related issues.

---

## Day 10

### Features
- Added AI integration using Ollama.
- Connected the project to the Gemma 3 local language model.
- Created a reusable AI provider module.
- Implemented AI-powered PDF summarization.
- Added PDF metadata extraction.
- Implemented text chunking for large PDF files.
- Refactored the project structure for better maintainability.
- Added type hints and improved code documentation.

### What I Learned
- How to integrate a local LLM into a Python application.
- How prompt engineering affects AI responses.
- Why modular architecture makes projects easier to maintain.
- The importance of splitting large documents before sending them to an AI model.
- How to build the foundation for AI-powered applications.

---

## Day 11

### Features
- Implemented multi-chunk AI summarization.
- Added progress display while summarizing PDF chunks.
- Improved project architecture by separating AI logic.
- Connected the application to the reusable chunk summarizer.
- Successfully generated AI summaries for multiple sections of a PDF.

### What I Learned
- Large documents should be processed in smaller chunks.
- Reusable functions make projects easier to extend.
- AI can process long documents step by step instead of all at once.
- A modular architecture improves maintainability and readability.

## Day 12

### Features
-Created a dedicated prompt management module (prompts.py).
-Separated AI prompts from business logic.
-Implemented hierarchical document summarization.
-Added final document summarization using AI.
-Improved the overall AI architecture.
-Reduced code duplication by reusing prompt templates.
-Prepared the project for future AI features (Quiz, Flashcards, Chat).

### What I Learned
-Prompt engineering should be separated from application logic.
-AI pipelines become easier to maintain with modular design.
-Hierarchical summarization produces better results for long documents.
-Reusable prompt templates simplify future feature development.
-Good software architecture makes AI projects easier to scale.

## Day 13

### Features
- Added AI-powered Quiz Generator.
- Created a dedicated `quiz_generator.py` module.
- Added a reusable quiz prompt template.
- Implemented automatic quiz generation from the final AI summary.
- Improved project architecture by separating quiz generation from the main application.
- Integrated the Quiz Generator into the main menu.
- Prepared the project for future AI learning features such as Flashcards and Chat with Notes.

### What I Learned
- Prompt engineering can be reused for different AI tasks.
- Generating quizzes from a final summary produces better questions than using raw document chunks.
- Separating features into dedicated modules improves readability and maintainability.
- A well-designed AI pipeline can support multiple learning tools with minimal code duplication.
- Building software incrementally leads to a cleaner and more scalable architecture.

## Day 14

### Features
- Added AI-powered Flashcard Generator.
- Created a reusable flashcard generation module.
- Integrated flashcard generation into the main application.
- Improved the application menu by adding a dedicated Flashcards option.
- Successfully generated study flashcards from AI-generated document summaries.

### What I Learned
- Flashcards are an effective way to reinforce learning from long documents.
- Reusing AI-generated summaries improves efficiency and reduces repeated processing.
- Modular design makes adding new AI features much easier.
- Prompt engineering has a significant impact on the quality and format of AI-generated flashcards.
