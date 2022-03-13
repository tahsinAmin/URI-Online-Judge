notes = {'W': 1, 'H': 1/2, 'Q': 1/4, 'E': 1/8, 'S': 1/16, 'T': 1/32, 'X': 1/64}

while True:
    s = input()
    if s == "*":
        break
    duration = 0
    a = s[1:-1].split("/")
    for element in a:
        cnt = 0
        for ltr in element:
            cnt += notes[ltr]
        duration += 1 if cnt == 1 else 0

    print(duration)
