# Project Specification

## Project Title
Offline Study Notes Structuring App

## Problem Statement
Students often collect study materials from multiple sources such as PDFs, handwritten notes, images, audio lectures, and plain text. These resources are unorganized, making revision difficult.

## Solution
Develop an offline AI-powered application that converts unstructured educational content into structured study notes using CPU-only inference.

## Objectives

- Work completely offline
- Run efficiently on CPU
- Support multiple input formats
- Generate structured notes
- Save results locally

## Target Users

- Students
- Teachers
- Self-learners

## Features

- PDF Upload
- Image Upload
- Audio Upload
- OCR
- Speech-to-Text
- AI Summarization
- Topic Extraction
- Flashcard Generation
- JSON Export
- SQLite Storage

## Tech Stack

Frontend:
- Streamlit

Backend:
- Python

AI:
- TinyLlama (GGUF)
- llama.cpp

OCR:
- Tesseract OCR

Speech:
- whisper.cpp

Database:
- SQLite

Output:
- JSON

## Constraints

- CPU Only
- Offline
- Open Source
- Fast Processing

## Success Criteria

- Accurate extraction
- Structured output
- CPU inference
- Offline execution