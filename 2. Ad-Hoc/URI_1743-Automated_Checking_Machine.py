a1,a2 = [],[]
flag = False

for i in input().split():
	a1.append(int(i))

for i in input().split():
	a2.append(int(i))

for i in range(5):
	if a1[i] == a2[i]:
		flag = True
		break

res = 'Y' if flag is False else 'N'
print(res)