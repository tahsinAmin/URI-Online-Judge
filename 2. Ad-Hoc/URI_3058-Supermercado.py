n = int(input())
p, g = map(float, input().split())
min_price = (p/g)*1000
n -= 1

for i in range(n):
    p, g = map(float, input().split())
    calc = (p/g)*1000
    min_price = calc if calc < min_price else min_price

print('{0:.2f}'.format(min_price))