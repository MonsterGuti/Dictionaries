characters = input().split(", ")
char_dict = {}

for char in characters:
    char_dict[char] = ord(char)

print(char_dict)