for i in range(int(input())):
	flag=0
	lang = []
	for j in range(int(input())):
		s = input()
		lang.append(s)
	result = 'ingles' if len(set(lang) > 1) else lang[0]
	print(result)