loop = int(input())

for i in range(loop):
	x,y =list(map(int, input().split()))
	raf = (3 * x) * (3 * x) + (y*y)
	bet = 2 * (x * x) + (5 * y) * (5 * y)
	car = -100 * x + (y * y * y)
	
	max_val = max(raf,bet,car)
	winner = 'Rafael' if raf is max_val else 'Beto' if bet is max_val else 'Carlos'
	print(winner, 'ganhou')