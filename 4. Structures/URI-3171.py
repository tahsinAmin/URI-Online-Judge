def check(n):
	dict[n] = True
	for i in list_of_lists[n]:
		if(dict[i] != True):
			check(i)
			
def connected():
	for i in dict:
		if(dict[i] == False):
			return False
	return True
	
list_of_lists = []
dict = {}

t, l = map(int, input().split())

for i in range(t):
	dict[i] = False
	list_of_lists.append([])
	
for i in range(l):
	x, y = map(int, input().split())
	x-=1
	y-=1
	list_of_lists[x].append(y)
	list_of_lists[y].append(x)
	
check(0)
print("COMPLETO" if connected() else "INCOMPLETO")