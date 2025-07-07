# This module contains functions for filtering student data.
from lib.student_data import display_students

def filter_students_by_major(student_list, major):
    filtered = [student for student in student_list if student[2] == major]

    if filtered:
        print(f"\nStudents majoring in {major}:")
        display_students(filtered)
    else:
        print(f"\nNo students found in {major}")

    return filtered

def student_generator(student_list, major):
    return(student for student in student_list if student[2] == major)


