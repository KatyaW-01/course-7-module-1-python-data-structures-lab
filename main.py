from lib.filters import filter_students_by_major, student_generator
from lib.student_data import students

filter_students_by_major(students, "Computer Science")

math_students = student_generator(students,"Mathematics")
print(next(math_students))
print(next(math_students))