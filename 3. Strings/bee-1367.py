n = int(input())
while n != 0:
    cnt, total = [0, 0]
    distinct_c = []
    distinct_inc = []
    for i in range(n):
        a, b, c = map(str, input().split())

        if(c == 'correct' and a not in distinct_c):
            cnt += 1
            distinct_c.append(a)
            total += int(b)
        elif(c == 'incorrect'):
            distinct_inc.append(a)

    for i in range(len(distinct_inc)):
        total += 20 if distinct_inc[i] in distinct_c else 0

    print(cnt, total)
    n = int(input())
