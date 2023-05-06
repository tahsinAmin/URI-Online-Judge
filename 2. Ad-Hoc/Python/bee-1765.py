t = int(input())

while t > 0:
    for i in range(t):
        q, a, b = map(float, input().split())
        result = q * (0.5 * (a+b) * 5)
        print(f"Size #{i+1}:")
        print('Ice Cream Used: {0:.2f} cm2'.format(result))

    print("")
    t = int(input())
