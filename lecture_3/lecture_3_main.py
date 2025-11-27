"""
Student Grade Analyzer
Program to manage and analyze student grades
"""


def display_menu():
    """Display the main menu options"""
    print("\n--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Generate a full report")
    print("4. Find the top student")
    print("5. Exit program")


def add_new_student(students):
    """Add a new student to the system"""
    name = input("Enter student name: ").strip()

    # Check if student already exists
    for student in students:
        if student["name"] == name:
            print("Student already exists.")
            return

    # Create new student dictionary
    new_student = {
        "name": name,
        "grades": []
    }
    students.append(new_student)
    print(f"Student '{name}' added successfully.")


def add_student_grades(students):
    """Add grades for a specific student"""
    if not students:
        print("No students available. Please add students first.")
        return

    name = input("Enter student name: ").strip()

    # Find the student
    student = None
    for s in students:
        if s["name"] == name:
            student = s
            break

    if not student:
        print("Student not found.")
        return

    print(f"Adding grades for {name}. Enter grades between 0-100 or 'done' to finish.")

    while True:
        grade_input = input("Enter a grade (or 'done' to finish): ").strip()

        if grade_input.lower() == 'done':
            break

        try:
            grade = int(grade_input)
            if 0 <= grade <= 100:
                student["grades"].append(grade)
                print(f"Grade {grade} added for {name}.")
            else:
                print("Invalid grade. Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 100.")


def generate_report(students):
    """Generate a report with all student averages and statistics"""
    if not students:
        print("No students available.")
        return

    averages = []
    print("\n--- Student Report ---")

    for student in students:
        if student["grades"]:
            try:
                average = sum(student["grades"]) / len(student["grades"])
                averages.append(average)
                print(f"{student['name']}'s average grade is {average:.1f}.")
            except ZeroDivisionError:
                print(f"{student['name']}'s average grade is N/A.")
        else:
            print(f"{student['name']}'s average grade is N/A.")

    if not averages:
        print("No grades available for any student.")
        return

    print("-" * 26)
    print(f"Max Average: {max(averages):.1f}")
    print(f"Min Average: {min(averages):.1f}")
    print(f"Overall Average: {sum(averages) / len(averages):.1f}")


def find_top_student(students):
    """Find the student with the highest average grade"""
    students_with_grades = [s for s in students if s["grades"]]

    if not students_with_grades:
        print("No students with grades available.")
        return

    # Use max with lambda function as specified
    top_student = max(students_with_grades,
                      key=lambda s: sum(s["grades"]) / len(s["grades"]))

    top_average = sum(top_student["grades"]) / len(top_student["grades"])
    print(f"The student with the highest average is {top_student['name']} with a grade of {top_average:.1f}.")


def main():
    """Main program function"""
    students = []  # List of dictionaries

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: ").strip())

            if choice == 1:
                add_new_student(students)
            elif choice == 2:
                add_student_grades(students)
            elif choice == 3:
                generate_report(students)
            elif choice == 4:
                find_top_student(students)
            elif choice == 5:
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()