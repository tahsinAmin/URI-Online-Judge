flag = 0
while True:
	n = int(input())
	if n == 0:
		break
	a=[]
	max=0
	for i in range(n):
		data = input()
		max = len(data) if len(data) > max else max
		a.append(data)
	if flag is 1:
		print()
	flag=1
	for i in range(n):
		print(a[i].rjust(max))