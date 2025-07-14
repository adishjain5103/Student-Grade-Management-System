import tkinter as tk
from tkinter import messagebox, scrolledtext

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

    def save_to_file(self, filename="students_gui.txt"):
        with open(filename, "a") as file:
            file.write(f"{self.roll},{self.name},{self.marks},{self.grade}\n")

def add_student():
    try:
        roll = entry_roll.get()
        name = entry_name.get()
        marks = list(map(int, [
            entry_marks1.get(),
            entry_marks2.get(),
            entry_marks3.get()
        ]))
        student = Student(roll, name, marks)
        student.save_to_file()
        messagebox.showinfo("Success", f"Student {name} added with Grade {student.grade}")
        clear_fields()
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric marks for all subjects.")

def view_students():
    try:
        with open("students_gui.txt", "r") as file:
            text_area.delete("1.0", tk.END)
            for line in file:
                roll, name, marks, grade = line.strip().split(",")
                text_area.insert(tk.END, f"Roll: {roll}, Name: {name}, Marks: {marks}, Grade: {grade}\n")
    except FileNotFoundError:
        messagebox.showinfo("Info", "No student records found.")

def clear_fields():
    entry_roll.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_marks1.delete(0, tk.END)
    entry_marks2.delete(0, tk.END)
    entry_marks3.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Student Grade Management System")
root.geometry("500x550")

# Input Fields
tk.Label(root, text="Roll No:").pack()
entry_roll = tk.Entry(root)
entry_roll.pack()

tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Marks 1:").pack()
entry_marks1 = tk.Entry(root)
entry_marks1.pack()

tk.Label(root, text="Marks 2:").pack()
entry_marks2 = tk.Entry(root)
entry_marks2.pack()

tk.Label(root, text="Marks 3:").pack()
entry_marks3 = tk.Entry(root)
entry_marks3.pack()

tk.Button(root, text="Add Student", command=add_student).pack(pady=5)
tk.Button(root, text="View All Students", command=view_students).pack(pady=5)

# Output Area
tk.Label(root, text="Student Records:").pack()
text_area = scrolledtext.ScrolledText(root, width=55, height=10)
text_area.pack(pady=10)

root.mainloop()
