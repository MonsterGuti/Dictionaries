elements = input().split()
bakery = {}

for index in range(0, len(elements), 2):
    key = elements[index]
    value = elements[index + 1]
    bakery[key] = int(value)

searched_products = input().split()
for product in searched_products:
    if product in bakery:
        quantity = bakery[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
