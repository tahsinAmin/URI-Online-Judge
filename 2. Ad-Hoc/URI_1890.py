cases = int(input())

for _ in range(cases):
    c, d = map(int, input().split())
    result = 0 if (c+d == 0) else 26**c * 10**d
    print(result)
