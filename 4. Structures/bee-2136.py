name, decision = map(str, input().split())
decisionary = {'NO': [], 'YES': []}
winner = ""

while True:
    try:
        if decision == 'YES':
            if name not in decisionary['YES']:
                decisionary['YES'].append(name)
                if len(name) > len(winner):
                    winner = name
        else:
            decisionary['NO'].append(name)
        name, decision = map(str, input().split())
    except ValueError:
        break

decisionary['YES'].sort()
decisionary['NO'].sort()

[print(i) for i in decisionary['YES']]
[print(i) for i in decisionary['NO']]
print(f"\nAmigo do Habay:\n{winner}")
