no_of_players, no_of_squares = map(int, input().split())
 
players_location = [0]*no_of_players
t1, t2, t3 = map(int, input().split())
traps = [t1, t2, t3]
no_dice_rolls = int(input())
pos = 0
for i in range(no_dice_rolls):
	d1, d2 = map(int, input().split())
	players_location[pos] += d1 + d2
	pos = (pos+1) % no_of_players
 
print(traps, players_location)
# time to make use of the traps