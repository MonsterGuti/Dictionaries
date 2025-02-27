number_of_commands = 0
my_dict = {}
metal = None
while True:
    command = input()
    if command == "stop":
        break
    number_of_commands += 1
    if number_of_commands % 2 != 0:
        metal = command
    else:
        number = int(command)
        my_dict[metal] = my_dict.get(metal, 0) + int(number)

for metal, number in my_dict.items():
    print(f"{metal} -> {number}")
