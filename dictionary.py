student_marks = {
    "Mehar": 87,
    "Aryan": 92,
    "Sana": 78,
    "Ishaan": 85,
    "Neha": 90
}

student_name = input("Enter the student's name: ")

if student_name in student_marks:
    print(f"{student_name}'s marks are: {student_marks[student_name]}")
else:
    print(f"Sorry, no marks found for '{student_name}'. Please check the name and try again.")