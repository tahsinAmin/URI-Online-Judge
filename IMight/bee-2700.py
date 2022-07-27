n = int(input())
a = []
totalPossible = 0
for i in range(n):
    listItem = [int(i) for i in input().split()]
    totalPossible += listItem[2]
    a.append(listItem)

max_total = 0
for i in range(n):
    summation = a[i][2]
    second_arr = [a[i]]

    for j in range(n):
        if(i != j):
            if ((a[i][0] == a[j][0] and a[i][1] == a[j][1]) or (a[i][0] > a[j][0] and a[i][1] > a[j][1]) or (a[i][0] < a[j][0] and a[i][1] < a[j][1])):
                summation += a[j][2]
                second_arr.append(a[j])

    # second_arr_len = len(second_arr)
    # for x in range(second_arr_len):
    #     for y in range(second_arr_len):
    #         if(x != y):
    #             if not ((a[x][0] == a[y][0] and a[x][1] == a[y][1]) or (a[x][0] > a[y][0] and a[x][1] > a[y][1]) or (a[x][0] < a[y][0] and a[x][1] < a[y][1])):
                #  Work here.

    if summation == totalPossible:
        max_total = totalPossible
        break
    else:
        max_total = max_total if max_total > summation else summation

print(max_total)


# 4
# 4 3 9
# 5 2 54
# 2 2 53
# 3 1 63
