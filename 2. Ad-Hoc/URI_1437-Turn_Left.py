while True:
    n = input()
    if n == "0":
        break
    pos = "N"
    inp = input()
    if len(inp) == int(n):
        for direction in inp:
            if direction == "E":
                pos = "O" if pos == "N" else "L" if pos == "S" else "N" if pos == "L" else "S"
            else:
                pos = "L" if pos == "N" else "O" if pos == "S" else "S" if pos == "L" else "N"
    print(pos)
