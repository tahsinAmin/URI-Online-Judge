notes = [3600,60,1]
val =[0,0,0]

remains = int(input())
for i in range(3): 
	if remains >= notes[i]:
		val[i] = remains // notes[i]
		remains = remains % notes[i]

print(f"{val[0]}:{val[1]}:{val[2]}\n")