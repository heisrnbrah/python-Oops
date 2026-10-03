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

# Insert student
cursor.execute("""
INSERT INTO students (
    full_name,
    date_of_birth,
    age,
    gender,
    mobile_number,
    email_address,
    password,
    preferred_language,
    school_college_name,
    class_grade,
    board_curriculum,
    academic_year
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "Aksin Rajan",
    "15-12-2006",
    19,
    "Male",
    "9747754375",
    "aksinrajan@gmail.com",
    "123456",
    "English",
    "Ilahia College",
    "BCA",
    "MGU",
    "2026"
))

# Save
conn.commit()

# Close
conn.close()

print("Table created and student inserted successfully!")