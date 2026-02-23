# ----------------------------------------------
# Author: Amanda Brock
# Date: February 22, 2026
# Assignment: Module 8.2
# Purpose: Load student.json, display original list,
# append a new student (if not duplicate),
# display updated list, and write changes back to student.json.
# ----------------------------------------------

import json
from pathlib import Path


def print_students(students):
    """Loops through the student list and prints each student in the required format."""
    for s in students:
        print(f"{s['L_Name']}, {s['F_Name']} : ID = {s['Student_ID']} , Email = {s['Email']}")


def main():
    file_path = Path(__file__).with_name("student.json")

    try:
        # Load JSON file
        with file_path.open("r", encoding="utf-8") as f:
            students = json.load(f)

        print("\n--- Original Student list ---")
        print_students(students)

        # New student record
        new_student = {
            "F_Name": "Amanda",
            "L_Name": "Brock",
            "Student_ID": 99999,
            "Email": "abrock@gmail.com"
        }

        # Prevent duplicates 
        if not any(s["Student_ID"] == new_student["Student_ID"] for s in students):
            students.append(new_student)

        print("\n--- Updated Student list ---")
        print_students(students)

        # Write updated list back to JSON file
        with file_path.open("w", encoding="utf-8") as f:
            json.dump(students, f, indent=4)

        print("\nNotification: student.json file was updated.")

    except FileNotFoundError:
        print(f"\nERROR: Could not find {file_path.name}.")
    except json.JSONDecodeError:
        print("\nERROR: student.json is not valid JSON.")
    except KeyError as e:
        print(f"\nERROR: Missing expected key in JSON data: {e}")


if __name__ == "__main__":
    main()