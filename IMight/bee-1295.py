from math import sqrt


def find_distance(x1, y1, x2, y2):
    return sqrt(((x1 - x2)**2) +
                ((y1 - y2)**2))


n = int(input())
while n > 0:
    a = []
    for i in range(n):
        e = list(map(float, input().split()))
        a.append(e)

    dist_arr = []
    min_distance = sqrt(((a[0][0] - a[1][0])**2) +
                        ((a[0][1] - a[1][1])**2))
    # min_distance = find_distance(a[0][0], a[0][1], a[1][0], a[1][1])
    for i in range(n):
        for j in range(i+1, n):
            some_val = find_distance(a[i][0], a[i][1], a[j][0], a[j][1])
            min_distance = some_val if some_val < min_distance else min_distance

    if min_distance < 10000:
        print("%.4f" % min_distance)
    else:
        print("INFINITY")

    n = int(input())


# 5
# 4610 406
# 538 4362
# 9614 6466
# 6246 2506
# 4660 411
# 0

# 1
# 10000.1 10000.3
# 0
