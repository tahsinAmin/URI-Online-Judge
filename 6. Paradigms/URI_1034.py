

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()]
    a.sort()
    cnt = 0
    flag = False
    min = m

    for i in range(n-1, -1, -1):
        if a[i] <= m:
            cnt = 0
            remains = m % a[i]
            print("remains value", remains)
            cnt += m // a[i]
            if remains == 0:
                if cnt < min:
                    min = cnt
                    # print(f"Min: ({min})")
                else:
                    break
                break
            else:
                for j in range(i-1, -1, -1):
                    print(
                        f'cout:({cnt}) Remains:({remains}) Min: ({min}) and value of a[j] is {a[j]}')
                    if a[j] <= remains:
                        if remains == a[j]:
                            # print("I'm inside")
                            cnt += 1
                            # flag = True
                            break
                        elif remains % a[j] == 0:
                            print("I'm inside")
                            cnt = cnt + remains // a[j]
                            if cnt < min:
                                min = cnt
                                print(f"Min: ({min})")
                            else:
                                break
        if cnt < min:
            min = cnt
            print(f"Min: ({min})")
        else:
            break

    print(min)
