notes = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
val =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

remains = float(input())

def loop(start, end, str):

	global remains
	for i in range(start, end): 
		if remains >= notes[i]:
			val[i] = int(remains / notes[i])
			remains = round(remains % notes[i], 2)
		
		print(f"{val[i]} {str}(s) de R$ {notes[i]:.2f}")

print("NOTAS:")
loop(0,6, "nota")

print("MOEDAS:")
loop(6,12, "moeda")

