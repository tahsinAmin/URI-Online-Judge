loop = int(input())

for i in range(loop):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    print(" ".join(str(x) for x in arr))
