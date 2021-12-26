while True:
    tickets, people = map(int, input().split())
    if tickets + people == 0:
        break
    data = [int(i) for i in input().split()]
    print(sorted(data))
