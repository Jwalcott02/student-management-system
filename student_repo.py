import sqlite3
from student import Student 

class StudentRepository:
    def __init__(self,db_name="students.db"):
        self.connecion = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()


def create_table(self):
    """Create students table if it does not exist """
    self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            age INTEGER NOT NULL,
            grade INTEGER NOT NULL
            
        )      
    """)
    self.connection.commit()

def add_student(self,student):
   """Add a new student to the database""" 
   self.cursor.execute("INSERT INTO students (student_id, name, age , grade) VALYES (?,?,?,?)",
                        (student.student_id, student.name, student.age , student.grade))
   self.connection.commit()

def get_students(self):
    """Fetch all students from the database"""
    self.cursor.execute("SELECT * FROM students")
    students = self.cursor.fetchall()
    return [Student(*student) for student in students]

def delete_student(self,student_id):
    self.cursor.execute("DELETE FROM students WHERE student_id = ?" , (student_id,))
    self.connection.commit()


def __del__(self):
    """Close database connection when object is destroyed"""
    self.connection.close()