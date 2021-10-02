n = int(input())
x = 0
while n!=0:
	for i in range(1,n+1):
		x=i
		for j in range(1,n+1):
			if i == j:
				x = 1
			print(("%3d" % (x)), end="")
			print("", end=" ") if(j < n) else print()
			x += (1 if j >= i else -1)
	print()
	n = int(input())