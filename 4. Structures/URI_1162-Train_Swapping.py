# for i in range(int(input())):
#     n = int(input())
#     a = [int(j) for j in input().split()]
#     cnt = 0
#     for j in range(n):
#         for k in range(j+1, n):
#             if a[j] > a[k]:
#                 a[j], a[k] = a[k], a[j]
#                 cnt += 1
#     print(f"Optimal train swapping takes {cnt} swaps.")


def mergeSort(arr):
    n = len(arr)
    if n == 1:
        return 0
    n1 = n//2
    n2 = n-n1
    arr1 = arr[:n1]
    arr2 = arr[n1:]
    print(f"arr1: {arr1}. arr2: {arr2}")
    ans = mergeSort(arr1) + mergeSort(arr2)

    i1, i2 = [0, 0]
    for i in range(n):
        if arr1[i1] > arr2[i2]:
            ans += n-i1
            i1 += 1
        else:
            i2 += 1
    return ans


print(mergeSort([3, 5, 6, 9, 1, 2, 7, 8]))
