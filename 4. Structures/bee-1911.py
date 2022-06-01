n = int(input())
while n != 0:
    attend = {}
    for i in range(n):
        data = input().split()
        attend[data[0]] = data[1]
    m = int(input())
    cnt = 0
    for i in range(m):
        data = input().split()
        if attend[data[0]] != data[1]:
            x, y = [attend[data[0], data[1]]]
            cnt2 = 0
            for j in range(len(x)):
                if x[j] != y[j]:
                    cnt2 += 1

            cnt += 1 if cnt2 > 1 else 0
    print(cnt)
    n = int(input())
