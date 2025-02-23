my_dict = {}

while True:
    command = input()
    if command == "statistics":
        break

    my_command = command.split(": ")
    key = my_command[0]
    quantity = my_command[1]

    if key not in my_dict:
        my_dict[key] = int(quantity)
    else:
        my_dict[key] += int(quantity)

print("Products in stock:")
for key, quantity in my_dict.items():
    print(f"- {key}: {quantity}")

print(f"Total Products: {len(my_dict.keys())}")
print(f"Total Quantity: {sum(my_dict.values())}")
