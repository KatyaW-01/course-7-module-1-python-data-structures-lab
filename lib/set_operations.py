# This module contains operations related to sets.
students = [
    (101, "Alice Johnson", "Computer Science"),
    (102, "Bob Smith", "Mathematics"),
    (103, "Charlie Davis", "Physics"),
    (104, "David Wilson", "Computer Science"),
    (105, "Eve Lewis", "Mathematics"),
]

def unique_majors(student_list):
   if len(student_list) == 0:
      return set()
   majors = set([student[2] for student in student_list])
   unique_majors = list(majors)
   print(unique_majors)
   return unique_majors

unique_majors(students)