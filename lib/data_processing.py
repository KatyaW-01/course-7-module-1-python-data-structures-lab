student = (101, "Alice Johnson", "Computer Science")

def format_student_data(student):
    sid = student[0]
    name = student[1]
    major = student[2]
    print (f"ID: {sid} | Name: {name} | Major: {major}")
    return (f"ID: {sid} | Name: {name} | Major: {major}")
   

def display_students(student_list):
    for student in student_list:
        format_student_data(student)

