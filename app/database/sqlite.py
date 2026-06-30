"""
SQLite database manager.
"""

import sqlite3
from pathlib import Path

DATABASE_PATH = Path("storage/database/notes.db")


class DatabaseManager:
    """Handles SQLite database operations."""

    def __init__(self):
        DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.connection.cursor()

    def create_table(self):
        """Create notes table."""

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            summary TEXT,
            json_output TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.connection.commit()

    def insert_note(self, title, summary, json_output):
        """Insert a processed note."""

        self.cursor.execute(
            """
        INSERT INTO notes(title, summary, json_output)
        VALUES (?, ?, ?)
        """,
            (title, summary, json_output),
        )

        self.connection.commit()

    def fetch_notes(self):
        """Return all saved notes."""

        self.cursor.execute("""
        SELECT * FROM notes
        ORDER BY created_at DESC
        """)

        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
