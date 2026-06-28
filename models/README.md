# AI Models

This directory contains all offline AI models used by the project.

## Models

| Model | Purpose |
|--------|---------|
| TinyLlama GGUF | Generate structured notes and summaries |
| Whisper Base EN | Speech-to-text transcription |
| Tesseract OCR | Extract text from images |

> Model files are not included in Git because they are large.

Run:

```bash
python scripts/download_models.py
```

to download them automatically.