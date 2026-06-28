# System Architecture

## Architecture Diagram

User

↓

Streamlit Interface

↓

Input Manager

↓

Extraction Layer

• PDF Parser

• OCR

• Audio Transcriber

↓

Text Cleaning

↓

Chunking

↓

TinyLlama

↓

JSON Generator

↓

SQLite Storage

↓

Structured Notes

## Modules

### Frontend
- Streamlit

### Extraction
- pdfplumber
- Tesseract
- Whisper

### AI Engine
- TinyLlama

### Storage
- SQLite

### Export
- JSON