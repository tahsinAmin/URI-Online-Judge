def check_one(matrix, m, n):
    check = [0]*10
    for x in range(m, m+3):
        for y in range(n, n+3):
            check[matrix[x][y]] += 1
            if check[matrix[x][y]] > 1:
                return False
    else:
        return True


def is_sudoku(matrix):
    for each_list in matrix:
        horizontal_array = [0]*9
        for element in each_list:
            horizontal_array[element-1] += 1
            if horizontal_array[element-1] > 1:
                return False

    for x in range(9):
        vertical_array = [0]*9
        for y in range(9):
            vertical_array[matrix[y][x]-1] += 1
            if vertical_array[matrix[y][x]-1] > 1:
                return False

    return True


n = int(input())
for k in range(n):
    arr = []
    for _ in range(9):
        arr.append([int(i) for i in input().split()])

    flag = True
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            if not check_one(arr, i, j):
                flag = False
                break
    if flag:
        flag = is_sudoku(arr)

    result = "SIM" if flag else "NAO"
    print(f'Instancia {k+1}\n{result}\n')