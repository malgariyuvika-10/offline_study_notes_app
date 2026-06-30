import sys
import os

# Ensure the app directory is in the system path so Python can find it
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.app import (
    AudioExtractor,
)  # Replace AudioExtractor with an actual class/function from your app.py


def test_app_imports_successfully():
    """Verify that the application components can be imported successfully."""
    # If the import above works, this test automatically passes!
    assert True