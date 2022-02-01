# while True:
n = int(input())
# if n == 0:
# break
arr = [0]*(n)
# print(arr)
rand_num = 1
i = 0
while True:
    if arr[i] == 0:
        arr[i] = 1
        if i == 12:
            if arr.count(0) == 0:
                print("Yes", arr)
                break
            else:
                print("No", arr)
                arr = [0]*(n)
                rand_num += 1
                i = 0

    i = (i + rand_num) % n
