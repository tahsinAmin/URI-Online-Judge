cases = int(input())
alpha = 'abcdefghijklmnoprstuvwxyz'

for _ in range(cases):
    s = input().lower()
    n = []
    for i in range(len(s)):
        if i in alpha and i not in n:
            n.append(i)

    if len(n) == 26:
        print("frase completa")
    elif len(n) >= 13:
        print('frase quase completa')
    else:
        print("frase mal elaborada")
