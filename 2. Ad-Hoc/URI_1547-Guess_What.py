tests = int(input())

for i in range(tests):
    data1 = input().split()
    data2 = input().split()
    dif = []
    
    for j in data2:
        dif.append(abs(int(j) - int(data1[1])))
    print(dif.index(min(dif)) + 1)