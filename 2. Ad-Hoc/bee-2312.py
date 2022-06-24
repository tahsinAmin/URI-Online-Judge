quantity = int(input())
complete = []
medals = []
auxiliar = []
contador = 0
for i in range(0, quantity):
    x = input()
    complete.append(x)
    x = x.split()
    games = [int(x[1]), int(x[2]), int(x[3])]
    if games in medals:
        contador += 1
    medals.append(games)


for j in range(0, len(medals)-contador):
    higher = max(medals)
    frequency = medals.count(higher)
    if frequency == 1:
        index = medals.index(higher)
        medals[index] = [-1]
        print(complete[index])
    elif frequency > 1:
        for k in range(frequency):
            index = medals.index(higher)
            auxiliar.append(complete[index])
            medals[index] = [-1]
        auxiliar.sort()
        for m in range(len(auxiliar)):
            print(auxiliar[m])
        auxiliar = []
