while True:
    try:
        m, n = list(map(int, input().split()))
        cnt = 0
        for i in range(m, n+1):
            cnt += 1 if len(str(i)) == len(set(str(i))) else 0

        print(cnt)
    except(EOFError):
        break
