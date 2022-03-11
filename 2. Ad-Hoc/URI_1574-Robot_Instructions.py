cases = int(input())
for _ in range(cases):
    pos = 0
    loop = int(input())
    arr = []

    for i in range(loop):
        ins = input()
        if ins == "LEFT":
            pos += -1
            arr.append(-1)
        elif ins == "RIGHT":
            pos += 1
            arr.append(1)
        else:
            if len(ins) == 10:
                idx = (int(ins[-2]) * 10) + (int(ins[-1]) - 1)
                arr.append(arr[idx])
                pos += arr[idx]
            else:
                idx = int(ins[-1]) - 1
                arr.append(arr[idx])
                pos += arr[idx]

    print(pos)
