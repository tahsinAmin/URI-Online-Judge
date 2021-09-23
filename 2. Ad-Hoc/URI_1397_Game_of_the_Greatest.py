turns = int(input())
while turns!=0:
	left,right = [0,0]
	while turns!=0:
		a,b = list(map(int,input(). split()))
		left += 1 if a>b else 0
		right += 1 if b>a else 0
		turns-=1
	print(left,right)
	turns = int(input())