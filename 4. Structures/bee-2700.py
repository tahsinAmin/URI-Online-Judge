n = int(input())
a = []
totalPossible = 0
for i in range(n):
    listItem = [int(i) for i in input().split()]
    totalPossible += listItem[2]
    a.append(listItem)

print(a, totalPossible)

max_total = 0
for i in range(n):
    for j in range(n):
        if(i != j):
            a[i][0] == a[j]
