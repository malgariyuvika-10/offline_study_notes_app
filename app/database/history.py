"""
History manager.
"""

import sqlite3
from pathlib import Path

DATABASE_PATH = Path("storage/database/notes.db")


class HistoryManager:
    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.connection.cursor()

    def log(self, note_id, action):
        """Store processing history."""

        self.cursor.execute(
            """
        INSERT INTO history(note_id, action)
        VALUES (?, ?)
        """,
            (note_id, action),
        )

        self.connection.commit()

    def get_history(self):
        """Return history records."""

        self.cursor.execute("""
        SELECT *
        FROM history
        ORDER BY timestamp DESC
        """)

        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
