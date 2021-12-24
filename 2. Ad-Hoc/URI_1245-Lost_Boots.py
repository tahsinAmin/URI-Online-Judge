while True:
    try:
        loop = int(input())

    except(EOFError):
        break
    d = []
    e = []
    for i in range(loop):
        m, n = input().split()
        m = int(m)
        if n == 'E':
            e.append(m)
        else:
            d.append(m)
    d.sort()
    e.sort()
    cnt = 0
    while len(d) != 0 and len(e) != 0:
        if d[len(d)-1] == e[len(e)-1]:
            cnt += 1
            d.pop()
            e.pop()
        elif d[len(d)-1] > e[len(e)-1]:
            d.pop()
        else:
            e.pop()
    print(cnt)
