for i in range(int(input())):
    data = input()
    num_str = ""
    for j in data:
        if j.isdigit():
            num_str += j
        else:
            num_str += " "
    print(sum(map(int, num_str. split())))