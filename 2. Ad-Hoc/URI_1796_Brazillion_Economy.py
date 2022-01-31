n = int(input())
data = [int(i) for i in input().split()]
cnt = 0
for i in data:
    cnt += 1 if i == 0 else 0
print("Y" if cnt > (n//2) else "N")
