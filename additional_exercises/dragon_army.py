dragons_info = {}

n = int(input())
for i in range(n):
    dragon_data = input().split()

    dragon_type = dragon_data[0]
    name = dragon_data[1]
    damage = int(dragon_data[2]) if dragon_data[2] != "null" else 45
    health = int(dragon_data[3]) if dragon_data[3] != "null" else 250
    armor = int(dragon_data[4]) if dragon_data[4] != "null" else 10

    if dragon_type not in dragons_info:
        dragons_info[dragon_type] = {}
    dragons_info[dragon_type][name] = (damage, health, armor)

for dragon_type in dragons_info:
    dragons = dragons_info[dragon_type]

    total_damage = sum(stats[0] for stats in dragons.values())
    total_health = sum(stats[1] for stats in dragons.values())
    total_armor = sum(stats[2] for stats in dragons.values())
    num_dragons = len(dragons)

    avg_damage = total_damage / num_dragons
    avg_health = total_health / num_dragons
    avg_armor = total_armor / num_dragons

    print(f"{dragon_type}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")

    for name in sorted(dragons.keys()):
        damage, health, armor = dragons[name]
        print(f"-{name} -> damage: {damage}, health: {health}, armor: {armor}")
