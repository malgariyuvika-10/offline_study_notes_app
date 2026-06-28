# 📚 Offline Study Notes Structuring App
### CPU-First • Offline AI • Structured Learning Engine

---

# Phase 1 – Plan & Specification

## Team Information

**Project Name:** Offline Study Notes Structuring App

**Hackathon Theme:** CPU-First Offline AI

**Platform:** Streamlit Web Application

**License:** GNU General Public License v3.0 (GPL-3.0)

---

# 1. Project Overview

## Problem Statement

Students often receive study materials in different unstructured formats such as:

- PDF Notes
- Handwritten Notes
- Lecture Audio
- Text Files
- Images

Organizing these materials manually is time-consuming and inefficient.

---

## Proposed Solution

The Offline Study Notes Structuring App is a CPU-first AI application that processes unstructured educational content locally and converts it into structured learning resources.

The application works completely offline without relying on any cloud APIs or internet connectivity.

The generated output includes:

- Structured Notes
- Topic-wise Headings
- Key Points
- Chapter Summary
- Flashcards (Question & Answer)
- Revision Notes
- JSON Structured Output

---

# 2. Objectives

The primary objectives are:

- Build a completely offline AI application.
- Ensure all inference runs on CPU.
- Support multiple educational input formats.
- Generate structured study notes.
- Store processed data locally.
- Demonstrate edge AI capabilities without cloud services.

---

# 3. Technical Constraints

## CPU First

No GPU or CUDA acceleration will be used.

Local inference only.

Models used:

- llama.cpp
- Whisper.cpp
- Tesseract OCR

---

## Offline First

The application will continue functioning when Wi-Fi is turned OFF.

No external API calls.

No OpenAI API.

No cloud inference.

---

# 4. Technology Stack

## Frontend

- Streamlit

Purpose:

- Upload files
- Display structured notes
- Download JSON output

---

## Backend

- Python 3.11

Framework:

- FastAPI (optional)
- Python Processing Pipeline

---

## AI Models

### Text Structuring

Runtime:
- llama.cpp

Model:
- TinyLlama 1.1B GGUF
OR
- Mistral 7B Quantized GGUF

Purpose:

- Generate summaries
- Extract headings
- Create flashcards
- Convert notes into structured JSON

---

### Audio Transcription

Runtime:

- Whisper.cpp

Purpose:

Convert lecture audio into text.

---

### OCR

Engine:

- Tesseract OCR

Purpose:

Extract text from images.

---

## PDF Processing

Library:

- pdfplumber

Purpose:

Extract text from PDF documents.

---

## Database

SQLite

Purpose:

Store:

- processed notes
- metadata
- generated JSON
- history

---

# 5. System Architecture

```
Input Layer
│
├── PDF
├── Images
├── Audio
├── Text Files
│
▼

Extraction Layer
│
├── pdfplumber
├── Tesseract OCR
├── Whisper.cpp
│
▼

Preprocessing
│
├── Cleaning
├── Chunking
├── Normalization
│
▼

AI Processing
│
├── llama.cpp
├── Prompt Engineering
├── JSON Structuring
│
▼

Storage
│
├── SQLite
├── JSON Files
│
▼

Output
│
├── Structured Notes
├── Summary
├── Flashcards
├── Revision Notes
└── Streamlit UI
```

---

# 6. Application Workflow

Step 1

User uploads:

- PDF
- Image
- Audio
- Text

↓

Step 2

Application detects file type.

↓

Step 3

Extract raw text using:

- OCR
- PDF Parser
- Whisper

↓

Step 4

Clean and normalize extracted text.

↓

Step 5

Send cleaned text to local llama.cpp model.

↓

Step 6

Generate:

- Structured Notes
- Summary
- Flashcards
- Key Concepts

↓

Step 7

Store output in SQLite.

↓

Step 8

Display results in Streamlit.

---

# 7. Structured Output Schema

```json
{
  "title": "",
  "topics": [
    {
      "heading": "",
      "summary": "",
      "key_points": []
    }
  ],
  "flashcards": [
    {
      "question": "",
      "answer": ""
    }
  ]
}
```

---

# 8. Local Storage

SQLite Database

Table:

notes

Columns:

- id
- title
- input_type
- created_at
- structured_json
- summary

---

# 9. Project Folder Structure

```
offline-study-notes-app/

│

├── streamlit_app/
│   └── app.py
│
├── backend/
│   ├── pipeline.py
│   ├── extractor_pdf.py
│   ├── extractor_image.py
│   ├── extractor_audio.py
│   ├── llm_engine.py
│   ├── schema_builder.py
│   ├── database.py
│   └── utils.py
│
├── models/
│   ├── llama.cpp/
│   └── whisper.cpp/
│
├── storage/
│   ├── notes.db
│   └── json/
│
├── tests/
│
├── README.md
├── SPEC.md
├── LICENSE
├── CONTRIBUTING.md
└── requirements.txt
```

---

# 10. Work Division

## Member 1

### AI & Backend

Responsibilities

- PDF Extraction
- OCR
- Whisper Integration
- llama.cpp Integration
- AI Pipeline
- SQLite

Estimated Time

8 Hours

---

## Member 2

### Frontend & DevOps

Responsibilities

- Streamlit UI
- File Upload
- JSON Display
- Download Feature
- Documentation
- GitLab CI

Estimated Time

8 Hours

---

# 11. GitLab Issues

| Issue | Assignee | Estimate |
|---------|----------|----------|
| PDF Extraction | Member 1 | 2 hrs |
| OCR Integration | Member 1 | 2 hrs |
| Whisper Integration | Member 1 | 3 hrs |
| llama.cpp Setup | Member 1 | 3 hrs |
| Prompt Engineering | Member 1 | 2 hrs |
| Backend Pipeline | Member 1 | 3 hrs |
| SQLite Storage | Member 1 | 2 hrs |
| Streamlit UI | Member 2 | 3 hrs |
| CLI Tool | Member 2 | 2 hrs |
| GitLab CI | Member 2 | 3 hrs |

---

# 12. Deliverables

- README.md
- SPEC.md
- Streamlit Web Application
- SQLite Database
- Structured JSON Output
- Offline CPU AI Inference
- GitLab Repository
- GPL-3.0 License

---

# 13. Validation Criteria

The project will be evaluated on:

- Accuracy of structured notes
- CPU performance
- Offline execution
- Memory efficiency
- JSON schema correctness
- Local data persistence

---

# 14. Offline Compliance

✅ No OpenAI API

✅ No Internet Required

✅ No Cloud Models

✅ CPU Only

✅ Local SQLite Storage

✅ Local AI Models

---

# 15. Future Enhancements

- Multi-language Support
- Handwritten Notes Recognition
- Smart Revision Scheduler
- Semantic Search
- Mobile Application
- Offline Vector Search

---

# Conclusion

The Offline Study Notes Structuring App demonstrates that modern AI applications can run efficiently on standard CPUs without requiring GPUs or cloud services. By combining lightweight local AI models with offline-first architecture, the project provides an accessible, privacy-preserving, and reliable educational assistant suitable for students in both connected and disconnected environments.