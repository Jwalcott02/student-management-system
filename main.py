from student_service import StudentService 

def main():
    service = StudentService()

    while True:
        print("\nStudent Managment System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Studen")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grade = int(input("Enter grade: "))
            print(service.add_student(name,age,grade))

        elif choice =="2":
            students = service.get_students()
            for student in students:
                print(student)

        elif choice =="3":
            student_id = int(input("Enter a Student ID to delete: "))
            print(service.delete_student(student_id))

        elif choice =="4":
            break

        else:
            print("Invalid choice. Try again. ")