elements = input().split()
my_bakery = {}

for element in range(0, len(elements), 2):
    key = elements[element]
    value = elements[element + 1]
    my_bakery[key] = int(value)

print(my_bakery)
