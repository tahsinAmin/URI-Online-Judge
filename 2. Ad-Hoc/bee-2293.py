n, m = map(int, input().split())
arr = []
max_val = 0
dic = {}
for i in range(n):
    inner_arr = []
    cnt = 0
    for j in input().split():
        k = int(j)
        inner_arr.append(k)
        dic[cnt] = k if cnt not in dic else dic[cnt] + k
        cnt += 1

    arr.append(inner_arr)
    result = sum(arr[i])
    max_val = max_val if max_val >= result else result

for i in range(m):
    k = dic[i]
    max_val = max_val if max_val >= k else k

print(max_val)
