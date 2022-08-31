while True:
    n = int(input())
    if n == 0:
        break
    highest = n

    while n > 1:
        if n % 2 == 0:
            n = n * 0.5
        else:
            n = n*3 + 1

        if n > highest:
            highest = n

    print(int(highest))
