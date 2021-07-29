import bisect

n,q = list(map(int, input().split()))
c=0
while n != 0 and q != 0:
	c+=1
	print("CASE# %d:" %c)
	l =[]
	for i in range(n):
		l.append(int(input()))
	
	l.sort()
	for i in range(q):
		item_to_find = int(input())
		index = bisect.bisect_left(l,item_to_find)
		# print('value from the bisect is', index)
		if index >= n or item_to_find != l[index]:
			print(item_to_find,'not found')	
		else:
			print(item_to_find, 'found at', index+1)
			
	n,q = list(map(int, input().split()))