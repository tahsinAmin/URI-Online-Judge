from math import sqrt
while True:
    try:
        a, b, c = list(map(float, input().split()))
        s = (a+b+c)/2
        s2 = s*(s-a)*(s-b)*(s-c)
        if(s2 < 0):
            print("-1.000")
        else:
            s3 = (4/3) * sqrt(s2)
            print(print("%.3f" % s3))
    except(EOFError):
        break
