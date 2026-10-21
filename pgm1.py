students = []

for student_number in range(1, 6):
    name = input(f"Enter the name of student {student_number}: ")
    
    while True:
        try:
            marks = float(input(f"Enter the marks of {name} (0-100): "))
            if 0 <= marks <= 100:
                break
            print("Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("Please enter a valid number. Try again.")

    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"

    students.append((name, marks, grade))

print("\nStudent Details")
print("-" * 42)
print(f"{'Name':<20}{'Marks':>10}{'Grade':>10}")
print("-" * 42)

for name, marks, grade in students:
    print(f"{name:<20}{marks:>10.2f}{grade:>10}")

print("-" * 42)
