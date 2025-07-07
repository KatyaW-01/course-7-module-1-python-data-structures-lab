students = [
    (101, "Alice Johnson", "Computer Science"),
    (102, "Bob Smith", "Mathematics"),
    (103, "Charlie Davis", "Physics"),
    (104, "David Wilson", "Computer Science"),
    (105, "Eve Lewis", "Mathematics"),
]

student_dict = {
    101: {"name": "Alice Johnson", "major": "Computer Science", "courses": {"CS101", "CS102"}},
    102: {"name": "Bob Smith", "major": "Mathematics", "courses": {"MATH101", "MATH102"}},
    103: {"name": "Charlie Davis", "major": "Physics", "courses": {"PHYS101", "PHYS102"}},
}

def display_students(student_list):
  print("\nStudent Records:")
  for sid, name, major in student_list:
    print(f"Id: {sid} | Name: {name} | Major: {major}")

def display_student_details(student_db):
  print("\nStudent Details:")
  for sid, details in student_db.items():
    print(f"ID: {sid} | Name: {details['name']} | Major: {details['major']} | Courses: {details['courses']}")

display_students(students)
display_student_details(student_dict)

