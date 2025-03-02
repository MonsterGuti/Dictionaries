number_of_commands = int(input())
parking = {}

for i in range(number_of_commands):
    command = input().split()
    username = command[1]

    if command[0] == "register":
        license_plate_number = command[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")

    elif command[0] == "unregister":
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")

for username, license_plate_number in parking.items():
    print(f"{username} => {license_plate_number}")
