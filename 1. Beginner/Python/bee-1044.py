x, y = map(int, input().split())
print("Sao Multiplos" if (y % x == 0 or x % y == 0) else "Nao sao Multiplos")
