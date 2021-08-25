n = int(input())
while n > 0:
	n-=1
	s = input()
	if len(s)  > 3:
		print(3)
	else:
		cnt = 0
		cnt += 1 if s[0] == 'o' else 0
		cnt += 1 if s[1] == 'n' else 0
		cnt += 1 if s[2] == 'e' else 0
		if cnt >=2:
			print(1)
		else:
			print(2)