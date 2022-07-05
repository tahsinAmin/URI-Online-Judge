def sum_line():
    for j in range(x):
        if 0 not in matrix[j]:
            return sum(matrix[j])
    return 0


def sum_column():
    for j in range(x):
        aux = []
        for m in range(x):
            aux.append(matrix[m][j])
        if 0 not in aux:
            return sum(aux)
    return 0


def sum_diagonal():
    s = 0
    for j in range(x):
        if matrix[j][j] != 0:
            s += matrix[j][j]
        else:
            return 0
    return s


def sum_diagonal_s():
    s = 0
    for j in range(x):
        if matrix[j][-1 - j]:
            s += matrix[j][-1 - j]
        else:
            return 0
    return s


def insert_in_line():
    for j in range(x):
        if matrix[j].count(0) == 1:
            matrix[j][matrix[j].index(0)] = total - sum(matrix[j])
    return matrix


def insert_in_column():
    for j in range(x):
        aux = []
        for m in range(x):
            aux.append(matrix[m][j])

        if aux.count(0) == 1:
            matrix[aux.index(0)][j] = total - sum(aux)
    return matrix


x = 3

matrix = [list(map(int, input().split())) for i in range(x)]
total = sum_line()
if not total:
    total = sum_column()
    if not total:
        total = sum_diagonal()
        if not total:
            total = sum_diagonal_s()
            if not total:
                for k in range(3):
                    total += sum(matrix[k])
                total //= 2

matrix = insert_in_line()
matrix = insert_in_column()
for k in range(x):
    print(*matrix[k])
