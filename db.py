import sqlite3

# Create / connect to database
conn = sqlite3.connect("student.db")

cursor = conn.cursor()

# Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT,
    date_of_birth TEXT,
    age INTEGER,
    gender TEXT,
    mobile_number TEXT,
    email_address TEXT UNIQUE,
    password TEXT,
    preferred_language TEXT,
    school_college_name TEXT,
    class_grade TEXT,
    board_curriculum TEXT,
    academic_year TEXT
)
""")

#DDL commands in DB.PY

# Save
conn.commit()

# Close
conn.close()

print("Table created and student inserted successfully!")