"""
WARNING: ONLY USE THIS TO DELETE VERY SPECIFIC DATA ELEMENTS. DO NOT REGULARLY RUN IT
"""

import sqlite3

db_filename = "database_logic/ai_memory.db"

conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS personality")

conn.commit()
conn.close()

print("Table 'personality' dropped successfully (if it existed).")

