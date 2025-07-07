from lib.filters import filter_students_by_major, student_generator
from lib.student_data import students, student_dict, display_students, display_student_details
from lib.set_operations import unique_majors, add_course
from lib.data_processing import format_student_data, display_students, student

#filters
filter_students_by_major(students, "Computer Science")

math_students = student_generator(students,"Mathematics")
print(next(math_students))
print(next(math_students))

#student_data
display_students(students)
display_student_details(student_dict)

#set_operations
unique_majors(students)
add_course(student_dict, 101, "CS201")

#data_processing
format_student_data(student)
display_students(students)