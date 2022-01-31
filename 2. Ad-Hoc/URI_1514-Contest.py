while True:
    everyone, problem = map(int, input().split())

    if everyone == problem == 0:
        break

    characteristics = 4
    arr = []
    flag1, flag4 = [True, True]

    for i in range(everyone):
        arr.append([int(j) for j in input().split()])

        if (arr[i].count(1) == problem and flag1):
            characteristics -= 1
            flag1 = False

        if (arr[i].count(1) < 1 and flag4):
            characteristics -= 1
            flag4 = False

    problemsAnswered = [0]*problem
    for i in range(problem):
        for j in range(everyone):
            problemsAnswered[i] += 1 if arr[j][i] == 1 else 0

    characteristics -= 1 if 0 in problemsAnswered else 0  # 2
    characteristics -= 1 if everyone in problemsAnswered else 0  # 3

    print(characteristics)
