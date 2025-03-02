phone_book_dict = {}

while True:
    command = input()
    if int(command.isdigit()):
        break
    line = command.split("-")
    name, number = line[0], line[1]
    phone_book_dict[name] = number

for acc in range(int(command)):
    acc_name = input()
    if acc_name not in phone_book_dict:
        print(f"Contact {acc_name} does not exist.")
        continue
    print(f"{acc_name} -> {phone_book_dict[acc_name]}")
