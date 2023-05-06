cnt = 1
while True:
    times = int(input().split())
    if times == 0:
        break
    a, b = [0, 0]
    while times > 0:
        x, y = map(int, input().split())
        a += x
        b += y
        times -= 1
        print(f"Teste {cnt}")

    if a > b:
        print("Aldo")
    elif b > a:
        print("Beto")
    else:
        print("0")
    print("")
