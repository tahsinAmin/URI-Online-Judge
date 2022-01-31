while True:
    try:
        data = input().split()
        volunteers = int(data[0])
        survival = int(data[1])
        list1 = [int(i) for i in input().split()]
        if volunteers == survival:
            s = set(list1)
            if len(s) == survival:
                print("*", end='')
        else:
            list1.sort()
            cnt = survival
            for i in range(1, volunteers+1):
                if cnt == 0:
                    break
                if i not in list1:
                    print(f'{i}', end=' ')
        print("")
    except(EOFError):
        break
