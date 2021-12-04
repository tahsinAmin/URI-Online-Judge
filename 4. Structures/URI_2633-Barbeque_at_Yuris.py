while True:
	try:
		loop = int(input())
	except(EOFError):
		break
	dict={}
	a=[]
	for i in range(loop):
		m,n = input().split()
		a.append(int(n))
		dict[int(n)] = m
	a.sort()
	
	print(' '.join(dict[i] for i in a))