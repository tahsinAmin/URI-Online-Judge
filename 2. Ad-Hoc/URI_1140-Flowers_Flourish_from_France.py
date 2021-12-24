while True:
    s = input().split()
    if s[0] == "*":
        break
    tautogram = s[0][0]
    flag = 1
    for i in s:
        if tautogram != i[0]:
            flag = 0
            break
    result = 'Y' if flag else 'N'
    print(result)
