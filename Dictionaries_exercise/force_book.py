force_dict = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if " | " in command:
        force_side, force_user = command.split(" | ")

        if not any(force_user in users for users in force_dict.values()):
            if force_side not in force_dict:
                force_dict[force_side] = []
            force_dict[force_side].append(force_user)

    elif " -> " in command:
        force_user, force_side = command.split(" -> ")

        for side in force_dict:
            if force_user in force_dict[side]:
                force_dict[side].remove(force_user)
                break

        if force_side not in force_dict:
            force_dict[force_side] = []

        force_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")


for side, users in force_dict.items():
    if users:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
