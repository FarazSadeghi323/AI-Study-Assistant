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

## Day 15

### Features
- Refactored the PDF processing workflow.
- Created a centralized `process_pdf()` function.
- Removed duplicated code from Summary, Quiz, and Flashcards features.
- Improved project architecture using Separation of Concerns.
- Simplified the main application logic.

### What I Learned
- Refactoring improves code quality without changing functionality.
- Avoiding duplicated code makes applications easier to maintain.
- Centralizing common logic reduces bugs and future development time.
- Clean architecture is essential for scalable software projects.

## Day 16

### Features
- Added Chat with Notes feature.
- Created a reusable AI chat module.
- Enabled users to ask questions about uploaded PDF documents.
- Implemented an interactive chat loop with exit support.
- Integrated Chat with Notes into the main application menu.
- Reused the centralized PDF processing pipeline.
- Improved application architecture by separating chat logic from the UI.

### What I Learned
- How to build an interactive AI conversation loop.
- Why separating business logic from the user interface improves maintainability.
- The importance of reusable modules in larger Python projects.
- How AI assistants can answer questions based on processed document summaries.

## Day 17

### Features
- Added a file management module.
- Implemented automatic result saving.
- Created a dedicated results folder.
- Saved AI summaries to summary.txt.
- Saved generated quizzes to quiz.txt.
- Saved generated flashcards to flashcards.txt.
- Improved project organization by separating file operations.

### What I Learned
- How to work with files using Python.
- How to automatically create folders with pathlib.
- Why separating file management logic improves code organization.
- How persistent outputs make AI applications more practical.

## Day 18

### Features
- Added Markdown export support.
- Saved AI summaries as both TXT and Markdown files.
- Saved quizzes as both TXT and Markdown files.
- Saved flashcards as both TXT and Markdown files.
- Extended the file manager with reusable Markdown saving functions.
- Improved compatibility with Markdown-based note-taking applications.

### What I Learned
- Markdown is a lightweight and widely supported documentation format.
- Exporting data in multiple formats improves usability.
- Reusable utility functions reduce duplicate code.
- Small improvements can significantly enhance the user experience.

## Day 19

### Features
- Added the first graphical user interface using CustomTkinter.
- Designed a modern dark-themed application window.
- Added navigation buttons for all project features.
- Connected the GUI to the existing application functions.

### What I Learned
- Learned the basics of CustomTkinter.
- Built a desktop GUI using object-oriented programming.
- Connected graphical components to existing backend logic.
- Improved the user experience by moving beyond a terminal interface.

## Day 20

### Features
- Added a status label to the graphical interface.
- Added a progress bar to improve user feedback.
- Implemented loading status updates.
- Connected the first GUI action with a background thread.
- Prevented the GUI from freezing while executing long-running tasks.
- Improved the application's responsiveness.

### What I Learned
- Learned how to use threads in Python GUI applications.
- Learned how to update GUI widgets dynamically.
- Improved the user experience with loading indicators.
- Understood the importance of keeping the GUI responsive during heavy operations.

# Day 21 – GUI Redesign and Application Layout

## Date
2026-07-29

## Goal
Redesign the desktop interface to provide a cleaner and more professional user experience.

## Completed

- Reorganized the GUI using a structured layout.
- Added a dedicated header section.
- Added a footer section.
- Added a status label.
- Added a progress bar.
- Created separate left and right panels.
- Moved all action buttons into the left panel.
- Added an output panel for displaying future AI results.
- Improved the overall application structure by splitting the interface into reusable methods.
- Added threaded execution for long-running operations to keep the interface responsive.
- Successfully tested the redesigned interface.

## Files Updated

- src/gui.py

## Result

The application now has a professional desktop layout that is much easier to extend with new AI features in the upcoming development days.

# Day 22 – GUI Integration & AI Summary Display

**Date:** July 31, 2026

## Today's Goal

Transform the AI Study Assistant from a console-based application into a desktop GUI application and integrate the PDF summarization pipeline.

---

## What I Implemented

### Desktop GUI

Built a modern desktop interface using **CustomTkinter**.

Features:

- Added application title
- Added subtitle
- Added status bar
- Added progress bar
- Two-column responsive layout
- Navigation buttons
- Output panel
- Footer

---

### Left Panel

Implemented buttons for:

- Summarize PDF
- Generate Quiz
- Generate Flashcards
- Chat with Notes
- Exit

---

### Right Panel

Implemented an Output Box using ScrolledText.

The application now displays:

- PDF information
- AI generated summary

instead of printing everything only inside the terminal.

---

### Background Processing

Used Python threading so the GUI does not freeze while the AI is generating responses.

---

### Progress Simulation

Implemented a fake loading system that updates:

- Processing PDF...
- Generating AI Response...
- Saving Results...
- Completed

using a progress bar.

---

### Summary Integration

Connected the GUI with the existing summarization pipeline.

Current workflow:

User clicks

Summarize PDF

↓

PDF processed

↓

AI summary generated

↓

Summary saved

↓

Summary displayed inside GUI

---

### Bug Fixes

Fixed multiple issues during integration.

Resolved:

- ImportError for pdf_info
- Wrong function name (show_output)
- Missing PDF metadata function
- GUI update issues
- Output rendering bugs

---

## Current Status

Completed:

- PDF processing
- AI summarization
- GUI interface
- Threading
- Output viewer
- TXT export
- Markdown export

The project now works as a real desktop application instead of a console script.

---

## Next Goal

Day 23

Implement the remaining AI tools inside the GUI:

- Generate Quiz
- Generate Flashcards
- Chat with Notes

and display their outputs inside the application.

# Day 23 – Connected AI Features to GUI

## Date
2026-08-01

## What I did

Today I completed the integration between the graphical user interface and the AI features.

### Improvements

- Connected the Quiz feature to the GUI.
- Connected the Flashcards feature to the GUI.
- Connected the Chat feature to the GUI.
- Added output display for all AI tools inside the Output Box.
- Fixed button callbacks to use GUI controller methods instead of calling backend functions directly.
- Improved communication between backend functions and the interface using return values.
- Displayed PDF information together with generated content.
- Fixed several GUI update issues.
- Verified that every feature works correctly after testing.

## Result

The application now provides a complete desktop interface where users can:

- Summarize PDF documents
- Generate quizzes
- Generate flashcards
- Chat with their study notes

without relying on terminal output.

## Next Goal

Improve the user experience by removing repeated PDF selection, redesigning the chat interface, and polishing the desktop application.

# Day 24 – GUI Improvements & Chat Integration

## Date
2026-08-02

## Completed

- Added "Select PDF" button to GUI.
- Users now select the PDF only once.
- Connected Summary, Quiz, Flashcards and Chat to the selected PDF.
- Removed repeated PDF selection dialogs.
- Added chat input field and Send button.
- Moved chat interaction from terminal to GUI.
- Integrated AI responses directly into the output panel.
- Improved desktop workflow and usability.
- Fixed GUI logic and callback issues.

## Files Updated

- src/gui.py
- src/main.py
- DEVLOG.md

## Notes

The application now behaves like a real desktop AI assistant.
Users can choose a PDF once and interact with all AI features from the graphical interface without using the terminal.


# Day 25 – Performance & User Experience Improvements

## Date
2026-08-03

## Completed

- Added PDF cache system to avoid repeated processing.
- Improved application performance.
- Added "Open Results Folder" button.
- Added "Clear Chat" feature.
- Enabled Enter key to send chat messages.
- Improved chat user experience with loading feedback.
- Refactored GUI workflow.

## Files Updated

- src/gui.py
- src/main.py
- DEVLOG.md

## Notes

Today's focus was improving application performance and user experience.
The PDF is now processed only once and reused across all AI features.
The desktop application feels much more responsive and closer to a production-ready release.

## 2026-08-01 — GUI Polish & Application Icon

### Completed
- Improved and finalized the CustomTkinter GUI.
- Added a custom application icon.
- Added the application icon asset under `assets/app_icon.png`.
- Integrated the custom icon into the main GUI window.
- Fixed GUI layout and geometry-manager issues.
- Fixed the chat interface so questions can be sent directly from the GUI.
- Verified PDF selection, summarization, quiz generation, flashcard generation, and chat functionality.
- Tested the complete GUI after the latest changes.
- Confirmed that all main GUI buttons are working correctly.

### Git
- Commit: `Complete GUI icon integration`
- Commit Hash: `6fee590`
- Changes pushed successfully to the `main` branch.

### Current Status
The GUI is now functional and visually polished, with a custom application icon and all major features working correctly.


## 2026-08-05 — Context-Aware Chat, Chat Management & v0.2.0

### Completed
- Added context-aware conversations for PDF chat.
- Added conversation history for each selected PDF.
- Improved the AI chat so follow-up questions can reference previous messages.
- Added support for contextual references such as:
  - "the second one"
  - "the first one"
  - "that"
  - "this"
  - "the previous one"
- Added Clear Chat functionality.
- Clear Chat now also removes the conversation history associated with the selected PDF.
- Added Copy, Paste, Cut, and Select All keyboard shortcuts to the chat input.
- Added Enter-to-send functionality for chat questions.
- Improved GUI button styling and application colors.
- Added consistent navy and yellow UI colors.
- Improved the overall chat interface and user experience.
- Tested context-aware follow-up questions successfully.
- Tested the updated GUI and chat management functionality.
- Verified that the main PDF features continue to work correctly.

### Git
- Added context-aware PDF chat feature.
- Added chat management functionality.
- Improved GUI styling.
- Changes merged into the `main` branch.
- Changes pushed successfully to GitHub.

### Release
- Version: `v0.2.0`
- Tag: `v0.2.0`
- Release message: `Release version 0.2.0`

### Current Status
The project now includes context-aware PDF conversations, chat history management, improved chat controls, and a more polished desktop GUI.

The `v0.2.0` milestone has been completed and pushed to GitHub successfully.

### Next Goals
- Improve AI response quality and reliability.
- Improve PDF question answering.
- Add more robust testing.
- Improve project documentation.
- Prepare the project for the `v1.0.0` release.

## 2026-08-11 — PDF Retrieval & Context-Aware Chat

### Completed
- Added a new PDF retrieval module for finding relevant document sections.
- Implemented keyword-based relevance scoring for PDF chunks.
- Added support for retrieving the most relevant chunks for each user question.
- Integrated PDF retrieval into the AI chat pipeline.
- Updated the chat system to use both the document summary and retrieved document sections.
- Improved question answering by providing the AI with more relevant information from the original PDF.
- Preserved conversation history and context-aware follow-up questions.
- Updated the main application to pass processed PDF chunks to the chat system.
- Tested the retrieval system with sample document chunks.
- Verified that irrelevant chunks are filtered out when answering questions.
- Tested the complete PDF chat workflow through the GUI.
- Confirmed that PDF retrieval and context-aware conversations work correctly.

### Technical Changes

#### New
- `src/ai/retriever.py`

#### Updated
- `src/ai/chat.py`
- `src/main.py`

### Retrieval Pipeline

The PDF chat system now follows this workflow:

PDF
→ Text Extraction
→ Text Chunking
→ Relevant Chunk Retrieval
→ Context-Aware AI Chat
→ Answer

Instead of relying only on the generated document summary, the system can now retrieve relevant sections from the original PDF based on the user's question.

### Git
- Branch: `feature/pdf-retrieval`
- Commit: `Add PDF retrieval to chat`
- Commit Hash: `4e72be6`
- Feature merged into `main`
- Changes pushed successfully to GitHub.

### Current Status
The project now includes a basic document retrieval layer that improves the accuracy and relevance of PDF-based conversations.

The AI Study Assistant is gradually moving from a simple PDF processing application toward a retrieval-based AI study system.

## Version 0.4.0 - Semantic Retrieval

### Added

- Added semantic embeddings using the `nomic-embed-text` model through Ollama.
- Added `embeddings.py` for generating text embeddings and calculating cosine similarity.
- Improved document retrieval using semantic similarity instead of relying only on keyword matching.
- Added hybrid retrieval that combines semantic similarity with keyword relevance.
- Added retrieval scores for better debugging and evaluation of document search results.
- Improved document chunking to create more meaningful and useful text sections.

### Improved

- Improved the accuracy of PDF question answering by retrieving more relevant document sections.
- Improved follow-up questions by using previous conversation context when building retrieval queries.
- Improved the chat system so questions such as "Explain that with a simple example" can use the previous conversation context.
- Improved the terminal chat workflow in `main.py`.

### Technical Details

- Local AI model: `gemma3:4b`
- Embedding model: `nomic-embed-text`
- Embedding vector size: 768
- Similarity method: Cosine Similarity
- Retrieval method: Hybrid Semantic + Keyword Retrieval
- Retrieval runs locally through Ollama.

### Example

The assistant can now identify that:

> "Why is giving different importance to assessment indicators useful?"

is semantically related to document sections discussing:

> assigning different weights to indicators based on their importance to improve assessment accuracy.

This allows the system to retrieve relevant information even when the user's question does not use exactly the same words as the document.

### Result

The PDF chat system now supports more intelligent semantic search, improved document retrieval, and better follow-up question understanding.

## Version 0.5.0 - Smart Study Tools GUI

### Added

- Added interactive quiz parsing with `quiz_parser.py`.
- Added interactive flashcard parsing with `flashcard_parser.py`.
- Added a complete GUI-based quiz experience.
- Added a complete GUI-based flashcard review experience.
- Added quiz scoring and percentage calculation.
- Added quiz explanations and answer feedback.
- Added quiz restart functionality.
- Added flashcard answer reveal and review-again functionality.
- Added PDF selection and integrated study tools into the GUI.

### Improved

- Improved the GUI layout and user interaction flow.
- Improved quiz generation by connecting generated AI output to the interactive quiz interface.
- Improved flashcard generation by connecting generated AI output to the interactive flashcard interface.
- Improved chat interaction with PDF documents.
- Improved GUI responsiveness and window interaction.
- Improved progress and status feedback during AI operations.
- Improved output handling for summaries, quizzes, flashcards, and chat responses.

### Study Tools

The application now provides three interactive study modes:

1. PDF Summary
2. Interactive Quiz
3. Study Flashcards
4. Chat with Notes

### Quiz Features

- Configurable number of questions.
- Difficulty selection.
- Interactive multiple-choice questions.
- Immediate answer feedback.
- Question explanations.
- Score calculation.
- Accuracy percentage.
- Quiz restart functionality.

### Flashcard Features

- Automatic flashcard generation from PDF documents.
- Interactive card-by-card review.
- Answer reveal functionality.
- Progress tracking.
- Review Again functionality.

### GUI Architecture

The GUI now integrates the main AI study features into a single desktop application:

PDF Selection
→ AI Processing
→ Study Tool Selection
→ Interactive Learning Experience

### Current Status

The AI Study Assistant has evolved from a basic PDF processing application into an interactive AI-powered study environment.

The project currently supports:

- PDF summarization
- Retrieval-based PDF chat
- Semantic document retrieval
- AI-generated quizzes
- Interactive quiz evaluation
- AI-generated flashcards
- Interactive flashcard review
- Desktop GUI

The next development phase will focus on improving the intelligence of the study tools, user experience, and overall application architecture.