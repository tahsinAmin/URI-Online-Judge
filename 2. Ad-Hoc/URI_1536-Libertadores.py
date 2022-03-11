cases = int(input())

for _ in range(cases):
    game1 = input()
    team1 = int(game1[0])
    team2 = int(game1[4])
    game2 = input()
    team2_ = int(game2[0])
    team1_ = int(game2[4])

    if team1 + team1_ > team2 + team2_:
        print("Time 1")
    elif team2 + team2_ > team1 + team1_:
        print("Time 2")
    else:
        if team2 > team1_:
            print("Time 2")
        elif team1_ > team2:
            print("Time 1")
        else:
            print("Penaltis")
