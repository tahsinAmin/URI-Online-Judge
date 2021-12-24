while True:
    loop = int(input())
    if loop == 0:
        break
    planet, count = ["", 2114]
    for i in range(loop):
        name, recieved, duration = input().split()
        if int(recieved) - int(duration) < count:
            count, planet = (int(recieved) - int(duration)), name
    print(planet)
