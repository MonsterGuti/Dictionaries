students = {}

while True:
    student_info = input()
    if ":" not in student_info:
        break
    name, ID, course = student_info.split(":")
    students[name] = (ID, course)

searched_course = student_info.replace("_", " ")

for name, (ID, course) in students.items():
    if course == searched_course:
        print(f"{name} - {ID}")
