n,k = [int(i) for i in input().split()]
names = []
for i in range(n):
	names.append(input())
	
names.sort()
print(names[k-1])