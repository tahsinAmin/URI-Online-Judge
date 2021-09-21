no_of_players, no_of_squares = map(int, input().split())
sum = no_of_players + no_of_squares
while sum is not 0:
	players_location = []
	[players_location.append({"trapped": False, "pos": 0}) for i in range(no_of_players)]
	t1, t2, t3 = map(int, input().split())
	traps = [t1, t2, t3]
	no_dice_rolls = int(input())
	
	index = 0
	for i in range(no_dice_rolls):
		d1, d2 = map(int, input().split())
		
		while players_location[index]["trapped"] ==  True:
			players_location[index]["trapped"] = False
			index = (index+1) % no_of_players
			
		players_location[index]["pos"] += d1 + d2
		if (players_location[index]["pos"] in traps):
			players_location[index]["trapped"] =  True
		
		if players_location[index]["pos"] > no_of_squares:
			print(index+1)
			break
		index = (index+1) % no_of_players
	
	no_of_players, no_of_squares = map(int, input().split())
	sum = no_of_players + no_of_squares