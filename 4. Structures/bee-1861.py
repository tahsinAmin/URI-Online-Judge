dict_of_murderers = {}
names = []

while True:
    try:
        murderer, murdered = input().split()
        if murderer in dict_of_murderers:
            if dict_of_murderers[murderer] != -1:
                dict_of_murderers[murderer] += 1
        else:
            dict_of_murderers[murderer] = 1
            names.append(murderer)

        dict_of_murderers[murdered] = -1
    except(EOFError):
        break

print("HALL OF MURDERERS")
names.sort()

for i in range(len(names)):
    val = dict_of_murderers[names[i]]
    if val > 0:
        print(f"{names[i]} {val}")
