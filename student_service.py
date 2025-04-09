from student_repo import StudentRepository
from student import Student

class StudentService:
    def __init__(self):
        self.repo = StudentRepository
    
    def add_student(self,name,age,grade):
        """Validating and adding students"""
        if age <= 15:
            return "Age must be greater than 15"
        if grade <= 70:
            return "Grade must be greater than 70"
        
        student = Student(None, name, age, grade)
        self.repo.add_student(student)
        return "Student added sucessfully"
    
    def get_students(self):
        """Fetching all the students"""
        return self.repo.get_students()
    
    def delete_student(self,student_id):
        """Deleting a student"""
        self.repo.delete_student(student_id)
        return "Student deleted sucessfully"
