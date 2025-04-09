# Student Management System 🧑‍🎓

A Python-based command-line Student Management System built using a Layered Architecture pattern (Presentation, Business Logic, Data Access).

## 📁 Project Structure
- `main.py` - CLI interface (Presentation Layer)
- `student_service.py` - Business logic for managing students
- `student_repo.py` - Handles SQLite data storage
- `student.py` - Student model

## 🔧 Features
- Add, view, and delete student records
- Data validation (age > 15, grade > 70)
- SQLite integration for persistent storage
- Clean separation of concerns

## 🚀 How to Run
1. Install Python 3.x
2. Run the program:
   ```bash
   python main.py

