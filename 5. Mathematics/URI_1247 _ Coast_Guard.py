import math

while True:
	try:
		d, vF, vG = map(int, input().split())

		tF = 12/vF
		h = math.sqrt(12*12 + d*d)
		tG = h/vG
		
		print("N" if tF < tG else "S")
	except(EOFError):
		break

		#  vF  (12) 
		#    ______
		#    |		/
		# 	 |   /
		# (d)|  / (h)
		# 	 | /
		# 	 |/
		#  vG