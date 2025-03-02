courses = {}

while True:
    command = input()
    if command == "end":
        break

    course_name, student_name = command.split(" : ")

    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

for course, student_names in courses.items():
    print(f"{course}: {len(student_names)}")
    for student in student_names:
        print(f"-- {student}")
