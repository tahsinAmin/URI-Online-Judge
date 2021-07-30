while True:
	h1,m1,h2,m2 = map(int, input().split())
	if h1 is 0 and h2 is 0 and m1 is 0 and  m2 is 0:
		break
	min = 0
	if(h1 is h2):
		if(m1 is m2):
			min = 1440
		if(m1 > m2):
			min = 1440 + (m2 - m1)
		else:
			min += (m2 - m1)
	elif(h1 < h2):
		min = (h2 - h1) * 60 + (m2 - m1)
	else:
		min = (24 - h1)*60 + (h2*60) + (m2 - m1)
	print(min)