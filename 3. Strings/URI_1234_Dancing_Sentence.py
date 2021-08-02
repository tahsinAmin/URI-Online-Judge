while True:
	try:
		str = input()
		new_str = ''
		flag = True
		for s in str:
			if s is ' ':
				new_str += ' '
			else:
				new_str += s.upper() if flag else s.lower()
				flag = not flag
		print(new_str)
	except(EOFError):
		break