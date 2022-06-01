x = int(input())


def digits():  # storing the password by analyzing the vector password
    global password, x
    numbers = []  # stores the password in fact
    for i in range(0, 6):
        highest = 0
        want = 0
        for j in range(0, x * 2):
            maior_novo = password[i].count(password[i][j])
            if maior_novo > highest:
                want = password[i][j]
                highest = maior_novo
        numbers.append(want)
    return numbers


cnt = 1
letters = ['A', 'B', 'C', 'D', 'E']
while x != 0:
    password = [[-1], [-1], [-1], [-1], [-1], [-1]]
    for i in range(0, x):
        phrase = str(input())
        phrase = phrase.replace(' ', '')
        for j in range(10, 16):
            if phrase[j] == 'A':
                password[j - 10].append(phrase[0])
                password[j - 10].append(phrase[1])
            elif phrase[j] == 'B':
                password[j - 10].append(phrase[2])
                password[j - 10].append(phrase[3])
            elif phrase[j] == 'C':
                password[j - 10].append(phrase[4])
                password[j - 10].append(phrase[5])
            elif phrase[j] == 'D':
                password[j - 10].append(phrase[6])
                password[j - 10].append(phrase[7])
            elif phrase[j] == 'E':
                password[j - 10].append(phrase[8])
                password[j - 10].append(phrase[9])

    numbers = digits()
    print('Teste', cnt)
    for i in range(0, 6):
        print(numbers[i], end=' ')
    print('')
    print('')
    x = int(input())
    cnt += 1
