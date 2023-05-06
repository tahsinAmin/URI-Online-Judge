j, rounds = list(map(int, input().split()))
arr = list(map(int, input().split()))
players = [0]*j
for i in range(j*rounds):
    players[i % j] += arr[i]

players = players[::-1]
print((j - players.index(max(players))))
