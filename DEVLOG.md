# AI Study Assistant - Development Log

## Day 1
- Created project structure
- Initialized Git repository
- Created GitHub repository

## Day 2
- Set up Python virtual environment
- Installed python-dotenv
- Created first executable version of the project

## Day 3
- Added interactive main menu
- Learned Git workflow (status, add, commit, push)

## Day 4
- Created pdf_reader.py
- Installed pypdf
- Learned Python modules and imports
- Added PDF page counter
- Successfully read the first PDF

## Notes
- Tested pypdf with a real PDF.
- Found compatibility issues with the sample file.
- Decided to migrate to PyMuPDF for better PDF support.

## Day 6

### Feature
- Migrated from pypdf to PyMuPDF.
- Implemented PDF text extraction.
- Improved PDF compatibility.

### What I Learned
- Different libraries have different strengths.
- Debugging is about finding the real cause.
- Choosing the right tool is part of software engineering.

## Day 7

### Feature
- Replaced pypdf with PyMuPDF.
- Successfully extracted text from a valid PDF.
- Added support for user-defined PDF paths.

### What I Learned
- Always verify the input before changing the code.
- Different PDF libraries have different compatibility.
- Debugging means finding the root cause, not guessing.

## Day 9

### Features
- Added PDF file picker using Tkinter.
- Added error handling for invalid PDF files.
- Improved application structure by separating functions.
- Successfully tested PDF text extraction with a valid PDF.

### What I Learned
- How to use Tkinter file dialogs.
- How to handle exceptions using try/except.
- The importance of testing with valid input data.
- How to debug file-related issues.

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