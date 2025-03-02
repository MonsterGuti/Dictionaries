legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_materials = {}

obtained = False
while not obtained:
    data = input().split()
    for i in range(0, len(data), 2):
        quantity = int(data[i])
        material = data[i + 1].lower()

        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                print(f"{legendary_items[material]} obtained!")
                key_materials[material] -= 250
                obtained = True
                break
        else:
            if material not in junk_materials:
                junk_materials[material] = 0
            junk_materials[material] += quantity

for material, quantity in key_materials.items():
    print(f"{material}: {quantity}")

for material, quantity in junk_materials.items():
    print(f"{material}: {quantity}")
