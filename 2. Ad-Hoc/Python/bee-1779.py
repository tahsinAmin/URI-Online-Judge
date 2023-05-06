def seq(arr, greatest_mean, n):
    cnt = 1
    contigeous_cnt = 1

    for i in range(arr.index(greatest_mean)+1, n):
        if arr[i] == greatest_mean:
            cnt += 1
        elif arr[i] != greatest_mean:
            if cnt > contigeous_cnt:
                contigeous_cnt = cnt
            cnt = 0
        if cnt > contigeous_cnt:
            contigeous_cnt = cnt
    return contigeous_cnt


for x in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    greatest_mean = max[arr]
    cnt = seq(arr, greatest_mean, n)
    print(f"Caso #{i+1}: {cnt}")
