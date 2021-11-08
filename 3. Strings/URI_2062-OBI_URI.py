n = int(input())
data = input().split()

for i in range(n):
   if len(data[i]) == 3 and data[i][0:2] in ["OB","UR"]:
   	data[i] =  data[i][0:2] + "I"

print(*data, sep = " ")