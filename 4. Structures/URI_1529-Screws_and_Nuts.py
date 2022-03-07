while True:
    try:
        n = int(input())
    except(EOFError):
        break
    except:
        continue

    d = []
    for i in range(n):
        x, y = map(int, input().split())
        [d.append(i) for i in range(x, y+1)]

    d.sort()
    num = int(input())
    count_num = d.count(num)
    if count_num != 0:
        start_index = d.index(num)
        end_index = start_index + count_num - 1
        print(f"{num} found from {start_index} to {end_index}")
    else:
        print(f"{num} not found")
