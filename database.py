import sqlite3

def get_connection():
    return sqlite3.connect("students.db")

def initialize_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                grade TEXT
            )
        ''')
        conn.commit()

def add_student(name, age, grade):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
        conn.commit()
        print("✅ Student added successfully.")

def view_students():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        if students:
            print("\n📄 Student Records:")
            for student in students:
                print(f"ID: {student[0]} | Name: {student[1]} | Age: {student[2]} | Grade: {student[3]}")
        else:
            print("⚠️ No student records found.")

def update_student(student_id, name, age, grade):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE students SET name = ?, age = ?, grade = ? WHERE id = ?", (name, age, grade, student_id))
        conn.commit()
        if cursor.rowcount:
            print("✅ Student updated.")
        else:
            print("❌ Student ID not found.")

def delete_student(student_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        if cursor.rowcount:
            print("🗑️ Student deleted.")
        else:
            print("❌ Student ID not found.")
