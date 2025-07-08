import sqlite3

DB_PATH = "bot.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                balance REAL DEFAULT 0
            )
        """)
        conn.commit()

def add_user(username):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        conn.commit()

def get_user(username):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return cursor.fetchone()

def update_balance(username, amount):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET balance = ? WHERE username = ?", (amount, username))
        conn.commit()