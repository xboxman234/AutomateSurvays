import sqlite3

db_filename = "database_logic/ai_memory.db"
info_file = "database_logic/general_infos/fivesurvays.txt"

# Connect to database
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS general_info (
    info_id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT NOT NULL,
    value TEXT
)
""")

# 1️⃣ DELETE EVERYTHING FIRST
cursor.execute("DELETE FROM general_info")

# 2️⃣ READ THE ENTIRE FILE AS ONE STRING
with open(info_file, "r", encoding="utf-8") as f:
    full_text = f.read().strip()

# 3️⃣ INSERT A SINGLE ROW
cursor.execute(
    "INSERT INTO general_info (key, value) VALUES (?, ?)",
    ("general_info", full_text)
)

conn.commit()
conn.close()

print(f"General info overwritten in '{db_filename}' successfully!")
