students = {}
languages = {}

while True:
    command = input()
    if command == "exam finished":
        break
    my_command = command.split("-")

    if len(my_command) == 3:
        username, language, points = my_command[0], my_command[1], int(my_command[2])
        if username in students:
            if points > students[username]:
                students[username] = points
        else:
            students[username] = points
        if language not in languages:
            languages[language] = 0
        languages[language] += 1

    elif len(my_command) == 2:
        username = my_command[0]
        del students[username]

print("Results: ")
for student, points in students.items():
    print(f"{student} | {points}")
print("Submissions:")
for language, submissions in languages.items():
    print(f"{language} - {submissions}")