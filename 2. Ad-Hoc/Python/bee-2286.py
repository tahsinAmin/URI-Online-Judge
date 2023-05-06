cnt = 1
n = int(input())
while n > 0:
    arr = []
    arr.append(input())
    arr.append(input())
    print(f"Teste {cnt}")
    for i in range(n):
        a, b = map(int, input().split())
        print(arr[(a+b) % 2])  # Power move of using index values
    cnt += 1
    print("")
    n = int(input())
