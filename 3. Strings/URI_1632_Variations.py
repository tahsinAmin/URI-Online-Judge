t = int(input())

for i in range(t):
	sample = input()
	list = [letters for letters in sample]
	result = 1
	
	for listItem in list:
		if listItem in ['A','a', 'E','e','I','i', 'O', 'o', 'S', 's']:
			result *= 3
		else:
			result *= 2
			
	print(result)