# This module contains operations related to sets.

def unique_majors(student_list):
   if len(student_list) == 0:
      return set()
   majors = set([student[2] for student in student_list])
   unique_majors = list(majors)
   print(unique_majors)
   return unique_majors

def add_course(student_db, student_id, new_course):
    if student_id in student_db:
        student_db[student_id]["courses"].add(new_course)
        print(f"\nAdded {new_course} to {student_db[student_id]['name']}'s courses.")
    else:
        print("\nStudent not found")
