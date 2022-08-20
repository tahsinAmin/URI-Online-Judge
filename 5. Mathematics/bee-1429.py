arr = [1, 0, 0, 0, 0, 0]
for i in range(1, 6):
    arr[i] = arr[i-1] * i

while(True):
    a = input()
    acm = 0
    if(a == '0'):
        break

    a = a[::-1]
    for i, j in enumerate(a):
        acm += int(j) * arr[i+1]

    print(acm)
