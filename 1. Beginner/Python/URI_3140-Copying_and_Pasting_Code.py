l = str(input())

while '<body>' not in l:
	l = str(input())
	
l = str(input())
	
while '</body>' not in l:
	print(l)
	l = str(input())