a = [0, 1]
for i in range(2, 42):
    a.append(a[i-1] + a[i-2])
a.pop(0)

while True:
    n = int(input())
    if n == 0:
        break
    print(a[n])
