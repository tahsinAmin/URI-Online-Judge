for i in range(int(input())):
	n = int(input())
	data = list(map(int, input().split()))
	b=sorted(data, reverse=True)
	unchanged=len(data)
	
	for i in range(len(data)):
		if data[i] is not b[i]:
			unchanged-=1
	print(unchanged)