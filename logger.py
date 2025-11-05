# logger.py
import sqlite3, os
from datetime import datetime

class Logger:
    def __init__(self, db_path="detections/logs.db"):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._create_table()

    def _create_table(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS detections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ts TEXT,
            class TEXT,
            confidence REAL,
            image_path TEXT
        )''')
        self.conn.commit()

    def log(self, cls, conf, img_path):
        c = self.conn.cursor()
        c.execute("INSERT INTO detections (ts, class, confidence, image_path) VALUES (?, ?, ?, ?)",
                  (datetime.now().isoformat(), cls, conf, img_path))
        self.conn.commit()
