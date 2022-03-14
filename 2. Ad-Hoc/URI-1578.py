x = 4
for _ in range(int(input())):
    rows_n_columns = int(input())
    arr = []
    for i in range(rows_n_columns):
        row = [(int(i)*int(i)) for i in input().split()]
        arr.append(row)

    print(f"Quadrado da matriz #{x}:")
    for i in range(rows_n_columns):
        for j in range(rows_n_columns):
            print(arr[i][j], end=" ")
        print("")
    x += 1
    print("")
