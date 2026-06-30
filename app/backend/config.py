"""
Configuration settings for the Offline Study Notes Structuring App.
"""

from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Storage directories
INPUT_DIR = BASE_DIR / "storage" / "input"
OUTPUT_DIR = BASE_DIR / "storage" / "output"
CACHE_DIR = BASE_DIR / "storage" / "cache"

# Database
DATABASE_PATH = BASE_DIR / "storage" / "database" / "notes.db"

# AI Models
LLAMA_MODEL_PATH = BASE_DIR / "models" / "tinyllama.gguf"
WHISPER_MODEL_PATH = BASE_DIR / "models" / "whisper-base.en.bin"

# Processing settings
MAX_CHUNK_SIZE = 1024
SUMMARY_LENGTH = 300

# Supported file formats
type=[
    "pdf",
    "png",
    "jpg",
    "jpeg",
    "txt",
    "wav",
    "mp3",
    "m4a",
    "flac"
]