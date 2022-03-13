while True:
    n = int(input())
    if n == 0:
        break
    else:
        data = [int(i) for i  in input().split()]
        b =  sorted(data)
        b.pop()
        print(data.index(b[len(b)-1]))