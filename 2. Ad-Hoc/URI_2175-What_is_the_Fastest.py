o,b,i = list(map(float, input().split()))
result = "Otavio" if o < b and o < i else "Bruno" if b < o and b < i else "Ian" if i < b and i < o else "Empate"
print(result)