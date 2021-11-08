list_of_names = []
while True:
	try:
		list_of_names.append(input())
	except(EOFError):
		break
	
working_list = [i.lower() for i in list_of_names]
result = working_list.index(max(working_list))
print(list_of_names[result])