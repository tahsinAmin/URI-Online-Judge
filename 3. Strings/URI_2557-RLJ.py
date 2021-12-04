while True:
	try:
		s= input()
		op,eq = [s.index("+"),s.index("=")]
		
		if "R" in s:
			print(int(s[eq+1:]) - int(s[op+1:eq]))
		elif "L" in s:
			print(int(s[eq+1:]) - int(s[:op]))
		else:
			print(int(s[:op]) + int(s[op+1:eq]))
	except(EOFError):
		break