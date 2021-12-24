for i in range(int(input())):
    data = input()
    if data[0] == data[2]:
        print(int(data[2]) * int(data[0]))
    elif data[1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(int(data[2]) - int(data[0]))
    else:
        print(int(data[2]) + int(data[0]))
