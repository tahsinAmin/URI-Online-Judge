for _ in range(int(input())):
    ax, ay, bx, by, cx, cy, dx, dy, rx, ry = map(int, input().split())
    if(ax <= rx <= bx and dx <= rx <= cx and ay <= ry <= dy and by <= ry <= cy):
        print(1)
    else:
        print(0)
