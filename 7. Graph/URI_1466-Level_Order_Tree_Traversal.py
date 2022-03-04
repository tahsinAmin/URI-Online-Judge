import queue


dic = {
    8:  [3, 10],
    3:  [1,  6],
    10: [0, 14],
    14: [13, 0],
    6:  [4,  7],
    13: [0,  0],
    7:  [0,  0],
    1:  [0,  0],
    4:  [0,  0]
}

q = [8]
while len(q) > 0:
    popNode = q.pop(0)
    print(f'{popNode if popNode != 0 else ""} ', end='')
    if dic[popNode][0] != 0:
        q.append(dic[popNode][0])
    if dic[popNode][1] != 0:
        q.append(dic[popNode][1])
print()

pN = 10
newValue = 9
if (newValue < pN):
    if dic[pN][0] == 0:
        dic[pN][0] = newValue
else:
    if dic[pN][1] == 0:
        dic[pN][1] = newValue
print(dic)
