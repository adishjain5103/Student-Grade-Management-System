class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        avg = sum(self.marks) / len(self.marks)
        if avg >= 90:
            return 'A'
        elif avg >= 75:
            return 'B'
        elif avg >= 60:
            return 'C'
        elif avg >= 40:
            return 'D'
        else:
            return 'F'

    def save_to_file(self, filename="students.txt"):
        with open(filename, "a") as file:
            file.write(f"{self.roll},{self.name},{self.marks},{self.grade}\n")

    def display(self):
        print(f"Roll No: {self.roll}, Name: {self.name}, Marks: {self.marks}, Grade: {self.grade}")


def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = list(map(int, input("Enter 3 subject marks separated by space: ").split()))
    student = Student(roll, name, marks)
    student.save_to_file()
    print("Student added successfully!\n")


def view_students(filename="students.txt"):
    print("\n----- Student Records -----")
    try:
        with open(filename, "r") as file:
            for line in file:
                roll, name, marks, grade = line.strip().split(",")
                print(f"Roll No: {roll}, Name: {name}, Marks: {marks}, Grade: {grade}")
    except FileNotFoundError:
        print("No records found yet.")
    print("----------------------------\n")


def main():
    while True:
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("Exiting Program.")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
