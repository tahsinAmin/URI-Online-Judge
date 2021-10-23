top = [0,1,3,5,10,25,50,100]
n = int(input())
if n >=1 and n<=100:
	for i in range(7):
		if n >= top[i] and n <= top[i+1]:
			print('Top', top[i+1])
			break