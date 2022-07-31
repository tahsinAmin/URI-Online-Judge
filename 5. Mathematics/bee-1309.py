while True:
    try:
        x = int(input())
        y = input()
        x = str(x)
        y = y if len(y) > 1 else ('0' + y)
        z = ''
        for i in range(len(x)-1, -1, -1):
            z_length = len(z)
            if z_length == 3 or z_length == 7 or z_length == 11:
                z = x[i] + ',' + z
            else:
                z = x[i] + z
        print(f'${z}.{y}')
    except EOFError:
        break
