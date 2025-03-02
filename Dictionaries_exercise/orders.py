product_price = {}
product_quantity = {}

while True:
    command = input()
    if command == "buy":
        break
    product = command.split()
    product_name, price, quantity = product[0], float(product[1]), int(product[2])
    if product_name not in product_quantity:
        product_quantity[product_name] = 0
    product_quantity[product_name] += quantity
    product_price[product_name] = price

for product in product_quantity:
    total_price = product_quantity[product] * product_price[product]
    print(f"{product} -> {(total_price):.2f}")
