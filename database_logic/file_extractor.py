import sqlite3
import json
import os

db_filename = "ai_memory.db"
json_filename = "ai_data.json"

# Connect to SQLite database
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

# Step 1: Get all table names, skipping unwanted ones
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
all_tables = [row[0] for row in cursor.fetchall()]
skip_tables = ["test_table", "sqlite_sequence"]  # tables to ignore
tables = [t for t in all_tables if t not in skip_tables]

# Step 2: Build fresh data dictionary
ai_data = {}

for table in tables:
    # Get column names
    cursor.execute(f"PRAGMA table_info({table})")
    columns = [col[1] for col in cursor.fetchall()]

    # Fetch all rows
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()

    table_data = []
    for row in rows:
        row_dict = dict(zip(columns, row))
        
        # Remove timestamp from memory table
        if table == "memory" and "timestamp" in row_dict:
            del row_dict["timestamp"]
        
        # Remove autoincrement IDs for cleaner JSON
        if table in ["personality", "memory", "general_info"]:
            id_fields = [k for k in row_dict.keys() if k.endswith("_id")]
            for k in id_fields:
                del row_dict[k]
        
        table_data.append(row_dict)
    
    # Remove duplicates within the table
    table_data = [dict(t) for t in {tuple(d.items()) for d in table_data}]
    
    ai_data[table] = table_data

conn.close()

# Step 3: Overwrite JSON with fresh data
with open(json_filename, "w", encoding="utf-8") as f:
    json.dump(ai_data, f, indent=4)

print(f"JSON file '{json_filename}' has been fully rewritten with current database data!")
