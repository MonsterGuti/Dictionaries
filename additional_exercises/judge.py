contests = {}
user_total_points = {}

while True:
    command = input()
    if command == "no more time":
        break
    username, contest, points = command.split(" -> ")
    points = int(points)

    if contest not in contests:
        contests[contest] = {}

    if username not in contests[contest]:
        contests[contest][username] = points
        user_total_points[username] = user_total_points.get(username, 0) + points
    else:
        if contests[contest][username] < points:
            user_total_points[username] -= contests[contest][username]
            contests[contest][username] = points
            user_total_points[username] += points

for contest in contests:
    print(f"{contest}: {len(contests[contest])} participants")
    sorted_participants = sorted(contests[contest].items(), key=lambda x: (-x[1], x[0]))
    index = 1
    for user, points in sorted_participants:
        print(f"{index}. {user} <::> {points}")
        index += 1

print("Individual standings:")
sorted_users = sorted(user_total_points.items(), key=lambda x: (-x[1], x[0]))
index = 1
for user, points in sorted_users:
    print(f"{index}. {user} -> {points}")
    index += 1
