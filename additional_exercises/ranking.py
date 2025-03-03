contests = {}

while True:
    command = input()
    if command == "end of contests":
        break
    contest, password = command.split(":")
    contests[contest] = password

users = {}

while True:
    command = input()
    if command == "end of submissions":
        break
    contest, password, username, points = command.split("=>")
    points = int(points)

    if contest in contests and contests[contest] == password:
        if username not in users:
            users[username] = {}

        if contest not in users[username] or users[username][contest] < points:
            users[username][contest] = points

best_user = None
best_points = 0

for user, contests in users.items():
    total_points = sum(contests.values())
    if total_points > best_points:
        best_user = user
        best_points = total_points

print(f"Best candidate is {best_user} with total {best_points} points.")
print("Ranking:")

for user in sorted(users):
    print(user)
    for contest, score in sorted(users[user].items(), key=lambda x: -x[1]):
        print(f"#  {contest} -> {score}")
