"""
WARNING: ONLY USE THIS TO DELETE VERY SPECIFIC DATA ELEMENTS. DO NOT REGULARLY RUN IT
"""

import sqlite3

db_filename = "ai_memory.db"

conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

# Delete the first 15 rows based on info_id
cursor.execute("""
DELETE FROM general_info
WHERE info_id IN (
    SELECT info_id
    FROM general_info
    ORDER BY info_id
    LIMIT 15
)
""")

conn.commit()
conn.close()

print("Deleted the first 15 rows from general_info successfully!")
