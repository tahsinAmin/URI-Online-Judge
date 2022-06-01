n, t0, l = list(map(int, input().split()))
A, B = [0, 0]

for i in range(n-1):
    sI = int(input())
    if abs(sI - t0) <= l:
        if i % 2 == 0:
            A += abs(sI - t0)
        else:
            B += abs(sI - t0)
        t0 = sI

print(A, B)
