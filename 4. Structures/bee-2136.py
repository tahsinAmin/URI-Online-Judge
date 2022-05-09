s = input()
yes_arr = []
no_arr = []
info = {}
winner = ""
while s != "FIM":
    data = s.split()
    if data[0] in info:
        info[data[0]] += 0 if data[1] == "NO" else 1
    else:
        if data[1] == "NO":
            no_arr.append(data[0])
            info[data[0]] = 0
        else:
            yes_arr.append(data[0])
            info[data[0]] = 1

    s = input()

a_name = ""
for x in yes_arr:
    if x in info:
        a_name = a_name if a_name else x
        if info[x] > 1:
            winner = x
            break
winner = winner if winner else a_name

yes_arr.sort()
no_arr.sort()
[print(i) for i in yes_arr]
[print(i) for i in no_arr]
print(f"\nAmigo do Habay:")
print(winner)
