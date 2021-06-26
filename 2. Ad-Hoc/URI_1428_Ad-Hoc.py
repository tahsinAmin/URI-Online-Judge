test = int(input())
for i in range(test):
	n, m = map(int, input().split())
	n = n//3
	m = m//3
	result = n * m
	print(result)