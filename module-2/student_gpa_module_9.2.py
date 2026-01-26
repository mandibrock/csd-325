# ----------------------------------------------
# Author: Amanda Brock
# Date: December 7, 2025
# Assignment: Module 9.2
# Purpose: Defines a student class to calculate and display a
# student's cumulative GPA. Prompts user for student info, credits,
# and course grades, then computes the GPA.
# ----------------------------------------------

# Student class to calculate cumulative GPA
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.total_credits = 0
        self.total_points = 0.0

    def add_course(self, credits, grade):
        grade_points = self.grade_to_points(grade)
        self.total_credits += credits
        self.total_points += grade_points * credits

    def grade_to_points(self, grade):
        grade = grade.strip().upper()
        mapping = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
        if grade not in mapping:
            print(f"Invalid grade '{grade}' entered. Assuming 0 points.")
        return mapping.get(grade, 0.0)

    def calculate_gpa(self):
        if self.total_credits == 0:
            return 0.0
        return self.total_points / self.total_credits

# Prompt user for student information
first_name = input("Enter the student's first name: ").strip()
last_name = input("Enter the student's last name: ").strip()

# Create a Student object
student = Student(first_name, last_name)

# Loop to input courses
while True:
    credits_input = input("Enter the course credits (number) or type 'done' to finish: ")
    if credits_input.lower() == 'done':
        break

    try:
        credits = float(credits_input)
    except ValueError:
        print("Invalid input. Please enter a number for credits.")
        continue

    grade = input("Enter the grade received (A-F): ")
    student.add_course(credits, grade)

# Display cumulative GPA
print(f"\n{student.first_name} {student.last_name}'s cumulative GPA is: {student.calculate_gpa():.2f}")