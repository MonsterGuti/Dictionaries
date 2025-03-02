companies_ID = {}

while True:
    command = input()
    if command == "End":
        break
    company, ID = command.split(" -> ")

    if company not in companies_ID:
        companies_ID[company] = []

    if ID not in companies_ID[company]:
        companies_ID[company].append(ID)

for company, ids in (companies_ID.items()):
    print(company)
    for emp_id in ids:
        print(f"-- {emp_id}")
