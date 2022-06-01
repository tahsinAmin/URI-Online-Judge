import math
a, b, c, d = map(int, input().split())

result = -1
if(c % a == 0):
    for i in range(a, c//2+1, a):
        if (i % b != 0 and c % i == 0 and d % i != 0):
            result = i
            break

    print(result)
