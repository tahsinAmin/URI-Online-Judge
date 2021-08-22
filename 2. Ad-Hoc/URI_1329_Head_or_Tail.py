n = int(input())
while n != 0:
	a = list(map(int, input().split()))
	m=0
	
	for i in range(n):
		m+= 1 if a[i] == 0 else 0
		
	j = n - m
	print("Mary won %d times and John won %d times" %(m,j))
	n = int(input())