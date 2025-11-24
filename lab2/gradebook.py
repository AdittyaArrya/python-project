# ----------------------------------------------------
# Title   : Gradebook Analyzer
# Author  : Aditya Arya
# Date    : 28 Oct 2025
# ----------------------------------------------------

# Menu
def print_menu():
    print("\nThis is a simple gradebook analysis tool that allows users to enter student marks, calculate statistics, assign grades, display results neatly.")
    print("\n====== Gradebook Usage Menu ======")
    print("1. Enter student marks manually")
    print("2. Exit")
    print("=================================")


# --- Task 2 ---


# Manual entry
def manual_entry():
    marks = {}
    while True:
        name = input("Enter student name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        else:
            score = float(input(f"Enter marks for {name}: "))
            marks[name] = score
    return marks


# --- Task 3 ---


# calculate average
def calculate_average(marks_dict):
    total = 0
    for score in marks_dict.values():
        total += score
    average = total / len(marks_dict)
    return average

# Calculate median
def calculate_median(marks_dict):
    sorted_marks = sorted(marks_dict.values())
    n = len(sorted_marks)
    if n % 2 == 1:  # odd number of elements
        median = sorted_marks[n // 2]
    else:  # even number of elements
        mid1 = sorted_marks[n // 2 - 1]
        mid2 = sorted_marks[n // 2]
        median = (mid1 + mid2) / 2
    return median

# Maximum score
def find_max_score(marks_dict):
    return max(marks_dict.values())

# Minimum score
def find_min_score(marks_dict):
    return min(marks_dict.values())


# --- Task 4 ---


# Grade Assignment
def assign_grades(marks_dict):
    grades = {}
    for name, mark in marks_dict.items():
        if mark >= 90:
            grade = "A"
        elif mark >= 80:
            grade = "B"
        elif mark >= 70:
            grade = "C"
        elif mark >= 60:
            grade = "D"
        else:
            grade = "F"
        grades[name] = grade
    return grades

# Grade distribution
def grade_distribution(grades_dict):
    distribution = {"A":0, "B":0, "C":0, "D":0, "F":0}
    for grade in grades_dict.values():
        if grade in distribution:
            distribution[grade] += 1
    return distribution


# --- Task 5 ---


# Pass/Fail student with name
def pass_fail_lists(marks_dict):
    passed_students = [name for name, mark in marks_dict.items() if mark >= 40]
    failed_students = [name for name, mark in marks_dict.items() if mark < 40]
    return passed_students, failed_students


# --- Task 6 ---


# Display result table
def display_results(marks, grades):
    print("\nName\t\tMarks\tGrade")
    print("---------------------------------")
    for name in marks:
        print(f"{name:<15}{marks[name]:<10}{grades[name]}")
    print("---------------------------------")

# --- Main Loop ---
def main():
    print("\n Welcome to the Gradebook Analyzer")

    while True:
        print_menu()
        choice = input("Enter your choice (1/2): ").strip()

        if choice == "1":
            marks = manual_entry()
        elif choice == "2":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

# --- Perform analysis ---
        avg = calculate_average(marks)
        med = calculate_median(marks)
        max = find_max_score(marks)
        min = find_min_score(marks)
        grades = assign_grades(marks)
        dist = grade_distribution(grades)
        passed, failed = pass_fail_lists(marks)

# --- Display results ---
        display_results(marks, grades)
        print(f"\n Statistics:")
        print(f"Average: {avg:.2f}")
        print(f"Median : {med:.2f}")
        print(f"Max: {max}")
        print(f"Min : {min}")
        print("\n Grade Distribution:")
        for grade, count in dist.items():
            print(f"  {grade}: {count} student")

        print(f"\n Passed ({len(passed)}): {', '.join(passed) if passed else 'None'}")
        print(f" Failed ({len(failed)}): {', '.join(failed) if failed else 'None'}")

        again = input("\nWould you like to analyze another dataset? (yes/no): ").lower()

        if again == 'yes':
            again = main()
        else:
            print("Thank you for using Gradebook Analyzer!")
        break

# start the program by calling main()
run = main()

