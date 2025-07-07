# This module contains functions for filtering student data.
from .student_data import display_students, students

def filter_students_by_major(student_list, major):
    filtered = [student for student in student_list if student[2] == major]

    if filtered:
        print(f"\nStudents majoring in {major}:")
        display_students(filtered)
    else:
        print(f"\nNo students found in {major}")

    return filtered

filter_students_by_major(students, "Computer Science")

def student_generator(student_list, major):
    return(student for student in student_list if student[2] == major)

math_students = student_generator(students,"Mathematics")
print(next(math_students))
print(next(math_students))
