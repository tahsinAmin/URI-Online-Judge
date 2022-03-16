x = 4
cases = int(input())
for m in range(cases):
    rows_n_columns = int(input())
    arr = []
    max_len_arr = [0]*rows_n_columns
    max_len = 0
    for i in range(rows_n_columns):
        row = []
        element = list(map(int, input().split()))
        for j in range(rows_n_columns):
            element[j] = element[j]*element[j]
            max_len = len(str(element[j])) if len(
                str(element[j])) > max_len else max_len
            max_len_arr[j] = len(str(element[j])) if len(
                str(element[j])) > max_len_arr[j] else max_len_arr[j]
            row.append(element[j])

        arr.append(row)

    print(f"Quadrado da matriz #{x}:")
    for i in range(rows_n_columns):
        for j in range(rows_n_columns-1):
            print(str(arr[i][j]).rjust(max_len_arr[j]), end=" ")
        print(str(arr[i][rows_n_columns-1]
                  ).rjust(max_len_arr[rows_n_columns-1]))
    x += 1
    if m != cases-1:
        print("")
