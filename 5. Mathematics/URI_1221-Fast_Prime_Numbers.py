def check_prime(n):
    if n == 2:
        return "Prime"
    elif n % 2 == 0 or n < 2:
        return "Not Prime"

    start = 3
    m = n ** (1/2)
    while start <= m:
        if n % start == 0:
            return "Not Prime"
        start += 2
    return "Prime"


for _ in range(int(input())):
    print(check_prime(int(input())))
