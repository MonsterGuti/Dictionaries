players_pool = {}

while True:
    command = input()
    if command == "Season end":
        break

    if "->" in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)

        if player not in players_pool:
            players_pool[player] = {}

        if position not in players_pool[player] or players_pool[player][position] < skill:
            players_pool[player][position] = skill

    elif "vs" in command:
        f_player, s_player = command.split(" vs ")

        if f_player in players_pool and s_player in players_pool:
            f_player_skills = 0
            s_player_skills = 0
            common_positions = False

            for position in players_pool[f_player]:
                if position in players_pool[s_player]:
                    common_positions = True
                    f_player_skills += players_pool[f_player][position]
                    s_player_skills += players_pool[s_player][position]

            if f_player_skills > s_player_skills:
                del players_pool[s_player]
            elif f_player_skills < s_player_skills:
                del players_pool[f_player]

total_skills = {}
for player, position in players_pool.items():
    total_skills[player] = sum(position.values())

sorted_players = sorted(total_skills.items(), key=lambda x: (-x[1], x[0]))

for player, skill in sorted_players:
    print(f"{player}: {skill} skill")
    sorted_positions = sorted(players_pool[player].items(), key=lambda x: (-x[1], x[0]))
    for position, skill in sorted_positions:
        print(f"- {position} <::> {skill}")
