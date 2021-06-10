import math
  
while True:
	try:
		num=input()
		ceil=math.ceil(int(num)/100)
		print(ceil)
	except (EOFError):
		break