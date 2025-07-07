student = (101, "Alice Johnson", "Computer Science")
students = [
    (101, "Alice Johnson", "Computer Science"),
    (102, "Bob Smith", "Mathematics"),
    (103, "Charlie Davis", "Physics"),
    (104, "David Wilson", "Computer Science"),
    (105, "Eve Lewis", "Mathematics"),
]

def format_student_data(student):
    sid = student[0]
    name = student[1]
    major = student[2]
    print (f"ID: {sid} | Name: {name} | Major: {major}")
    return (f"ID: {sid} | Name: {name} | Major: {major}")
   

def display_students(student_list):
    for student in student_list:
        format_student_data(student)

format_student_data(student)
display_students(students)