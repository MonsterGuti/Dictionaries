total_tests = int(input())
student_grades = {}
student_tests = {}

for i in range(total_tests):
    test_count = 0
    student_name = input()
    grade = float(input())

    if student_name not in student_grades:
        student_grades[student_name] = 0
        student_tests[student_name] = 0
    student_grades[student_name] += grade
    student_tests[student_name] += 1

for student in student_grades:
    if student_grades[student] / student_tests[student] >= 4.50:
        student_avg_grade = student_grades[student] / student_tests[student]
        print(f"{student} -> {(student_avg_grade):.2f}")