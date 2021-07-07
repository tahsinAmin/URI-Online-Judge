while True:
	n = int(input())
	if n != 0:
		result = (n * (n + 1) * (2*n + 1)) // 6
		print(result)
	else:
		break