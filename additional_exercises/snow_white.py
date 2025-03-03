dwarf_info = {}
hat_color_count = {}

while True:
    command = input()
    if command == "Once upon a time":
        break
    name, hat_color, physics = command.split(" <:> ")
    physics = int(physics)

    if (name, hat_color) not in dwarf_info:
        dwarf_info[name, hat_color] = physics
    else:
        if dwarf_info[name, hat_color] < physics:
            dwarf_info[name, hat_color] = physics

    if hat_color not in hat_color_count:
        hat_color_count[hat_color] = 0
    hat_color_count[hat_color] += 1

sorted_dwarfs = sorted(dwarf_info.items(), key=lambda x: (-x[1], -hat_color_count[x[0][1]]))

for (name, hat_color), physics in sorted_dwarfs:
    print(f"({hat_color}) {name} <-> {physics}")
