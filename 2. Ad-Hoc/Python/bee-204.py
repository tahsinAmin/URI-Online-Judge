amount, tries = map(int, input().split())
bankanary = {'D': amount, 'E': amount, 'F': amount}

for i in range(tries):
    a_round = input().split()
    if(a_round[0] == 'C'):
        # PURCHASE
        bankanary[a_round[1]] -= int(a_round[2])
    elif a_round[0] == 'V':
        # SELL
        bankanary[a_round[1]] += int(a_round[2])
    elif a_round[0] == 'A':
        # RENT
        bankanary[a_round[1]] += int(a_round[3])
        bankanary[a_round[2]] -= int(a_round[3])

print(bankanary['D'], bankanary['E'], bankanary['F'])
