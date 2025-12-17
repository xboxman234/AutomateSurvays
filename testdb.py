import sqlite3
import os

# Database filename
db_filename = "ai_memory.db"

# Connect (creates file if it doesn't exist)
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

# Create a table (if it doesn't exist)
cursor.execute("""
CREATE TABLE IF NOT EXISTS test_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT
)
""")

# Insert a single row
cursor.execute("INSERT INTO test_table (content) VALUES (?)", ("Hello, AI memory!",))

conn.commit()

# Fetch and print all rows
cursor.execute("SELECT * FROM test_table")
rows = cursor.fetchall()

print("Current contents of test_table:")
for row in rows:
    print(row)

conn.close()

# Confirm the database file exists
if os.path.exists(db_filename):
    print(f"\nDatabase file '{db_filename}' created successfully!")
