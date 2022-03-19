for _ in range(int(input())):  # test cases
    fruits = {}

    for __ in range(int(input())):  # items
        m, n = input().split()
        fruits[m] = float(n)

    price = 0
    for __ in range(int(input())):  # quantity
        m, n = input().split()
        price += fruits[m] * int(n)

    print('R$ %.2f' % price)
