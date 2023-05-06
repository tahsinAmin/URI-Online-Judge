n = int(input())
arr = []
basket = []
for i in range(n):
    arr.append([int(x) for x in input().split()])

for i in range(2*n):
    x, y = map(int, input().split())
    basket.append(arr[x-1][y-1])

print(len(set(basket)))
