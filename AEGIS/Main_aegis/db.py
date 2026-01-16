
import sqlite3
from datetime import datetime
from spinal_code import classify_query

DB_NAME = "aegis.db"

def get_db_connection():
    """Establishes a connection to the SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    """Creates the queries table if it doesn't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME NOT NULL,
            query TEXT NOT NULL,
            result TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_query(query: str, result: str):
    """Saves a query and its result to the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    timestamp = datetime.now()
    cursor.execute(
        "INSERT INTO queries (timestamp, query, result) VALUES (?, ?, ?)",
        (timestamp, query, result)
    )
    conn.commit()
    conn.close()

def get_recent_queries(n: int = 10):
    """Retrieves the N most recent queries from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, query, result FROM queries ORDER BY timestamp DESC LIMIT ?", (n,))
    queries = cursor.fetchall()
    conn.close()
    return queries

def process_and_save_query(query: str):
    """
    Processes a query to get its classification and saves it to the database.
    """
    result = classify_query(query)
    save_query(query, result)
    print(f"Saved query: '{query}' with result: '{result}'")

if __name__ == '__main__':
    # Initialize the database and table when run as a script
    create_table()
    print("Database and table initialized.")

    # Example usage:
    # You can uncomment the following lines to test the functionality
    test_query = "What is the meaning of life?"
    process_and_save_query(test_query)
    recent_queries = get_recent_queries()
    for row in recent_queries:
        print(dict(row))
