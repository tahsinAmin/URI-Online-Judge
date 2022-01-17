loop = int(input())
cnt, total_mass, total_money = [0, 0, 0]
for i in range(loop):
    total_money += float(input())
    quantity = len(input().split())
    total_mass += quantity
    print(f'day {i+1}: {quantity} Kg')

print(f'{round((total_mass/loop),2)} Kg by day')
print(f'R$ {round((total_money/loop),2)} by day')
