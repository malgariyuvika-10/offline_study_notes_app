-- Notes Table

CREATE TABLE IF NOT EXISTS notes (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT NOT NULL,

    summary TEXT,

    json_output TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

-- Processing History

CREATE TABLE IF NOT EXISTS history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    note_id INTEGER,

    action TEXT,

    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(note_id)
        REFERENCES notes(id)

);