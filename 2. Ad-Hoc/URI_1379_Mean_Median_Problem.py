while True:
    a, b = list(map(int,input().split()))
    if a == 0 and b == 0:
        break
    c = min(a,b)*3 - (a + b)
    print("Min value is %d" % c)