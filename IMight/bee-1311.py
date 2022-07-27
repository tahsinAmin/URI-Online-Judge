while True:
    s, b = map(int, input().split())
    if s+b == 0:
        break
    soldier_left, soldier_right = [1, s]
    [mini, maxi] = [soldier_left, soldier_right]

    for i in range(b):
        x, y = map(int, input().split())

        if x > mini:
            if (x - 2 == mini and x == maxi):
                soldier_left = mini
            elif(x-1 != mini):
                soldier_left = mini
            else:
                soldier_left = x-1
        else:
            if (mini >= x - 1):
                soldier_left = '*'

        if y < maxi:
            if (y == mini and y + 2 == maxi):
                soldier_right = y+1
            else:
                soldier_right = y+1
        else:
            if (maxi <= y + 1):
                soldier_right = '*'

        print(f'{soldier_left} {soldier_right}')

        if (soldier_left == '*'):
            mini = soldier_right
        if (soldier_right == '*'):
            maxi = soldier_left

        print(soldier_left, soldier_right, mini, maxi)

    print('-')


#  Probably to have a left range and right range

# 10 4
# 1 7   => * 8
# 8 8   => * 9
# 9 9   => * 10
# 10 10 => * *
# 0 0

# 10 4
# 2 5    => 1 6
# 6 9    => 1 10
# 1 1    => * 10
# 10 10  => * *
# 0 0
