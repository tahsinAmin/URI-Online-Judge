def count_keys(dict, val):
    cnt = 0
    for key, value in dict.items():
        cnt += 1 if value > val else 0
    return cnt


while True:
    tickets, people = map(int, input().split())
    if tickets + people == 0:
        break
    data = [int(i) for i in input().split()]
    dict = {}
    for i in data:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    print(count_keys(dict, 1))
