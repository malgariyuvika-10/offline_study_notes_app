"""
Helper utility functions.
"""

import os
from pathlib import Path


def ensure_directory(path: str):
    """
    Create directory if it doesn't exist.
    """
    Path(path).mkdir(parents=True, exist_ok=True)


def get_file_extension(file_path: str) -> str:
    """
    Return file extension.
    """
    return os.path.splitext(file_path)[1].lower()


def is_supported_file(file_path: str, supported_formats: list) -> bool:
    """
    Check if uploaded file is supported.
    """
    extension = get_file_extension(file_path)
    return extension in supported_formats


def read_text_file(file_path: str) -> str:
    """
    Read a text file.
    """
    with open(file_path, encoding="utf-8") as file:
        return file.read()
