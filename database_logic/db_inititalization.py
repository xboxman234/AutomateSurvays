import sqlite3

db_filename = "ai_memory.db"
info_file = "thingstoknow.txt"

# Connect to database
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

# Create general_info table
cursor.execute("""
CREATE TABLE IF NOT EXISTS general_info (
    info_id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT NOT NULL,
    value TEXT
)
""")

# Read the text file
with open(info_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    if not line or line.startswith("#"):
        continue  # skip empty lines and comments

    # Special parsing
    if line.startswith("pets,"):
        key = "pets"
        value = line.replace("pets,", "").strip()
    elif "postal code" in line:
        key = "postal_code"
        value = line.split("postal code")[-1].split(",")[0].strip()
    elif "date of birth" in line:
        key = "date_of_birth"
        value = line.split("date of birth")[-1].split(",")[0].strip()
    elif "first name" in line:
        key = "first_name"
        value = line.split("first name")[-1].split("last name")[0].strip()
        # handle last name
        last_name = line.split("last name")[-1].strip()
        cursor.execute("INSERT INTO general_info (key, value) VALUES (?, ?)", ("last_name", last_name))
    elif "male" in line or "female" in line:
        # Handle gender and children age info together
        key = "gender_children"
        value = line
    else:
        # Generic parsing: take everything before "is" as key, after as value
        if " is " in line:
            key = line.split(" is ")[0].replace("your ", "").replace("the ", "").replace("you ", "").strip().replace(" ", "_")
            value = line.split(" is ")[1].strip()
        else:
            key = line.replace(" ", "_")
            value = line

    cursor.execute("INSERT INTO general_info (key, value) VALUES (?, ?)", (key, value))

conn.commit()
conn.close()
print(f"General info from '{info_file}' added to '{db_filename}' successfully!")
