while True:
    x = input()
    if x == '0':
        break
    else:
        x, y, z = map(int, x.split())
        result = (x*y*z)//(z-x)
        print(result, end='')
        if result == 1:
            print(' pagina')
        else:
            print(' paginas')
z