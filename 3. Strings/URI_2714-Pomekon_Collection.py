a=[]
for i in (int(input())):
   a.append(input())

distinctP = len(set(a))
print("Falta(m) {} pomekon(s).".format(151-distinctP))
