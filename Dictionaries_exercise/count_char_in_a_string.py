user_input = input()
my_dict = {}

for char in user_input:
    if char == " ":
        continue
    current_char = char
    count_char = 0
    for j in user_input:
        if j == current_char:
            count_char += 1
    my_dict[char] = count_char

for char, count_char in my_dict.items():
    print(f"{char} -> {count_char}")
