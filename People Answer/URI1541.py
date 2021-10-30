# https://github.com/Matuiss2/URI-ONLINE/blob/master/1400-%201599/1542.py


import math
while True:
    '''i had q for everything in a variable because of the closing condition
 if i divided into 3 variables before it would give error in the last input'''
    data = list(map(int, input(). split()))
    if data[0] == 0:
        break
    a = data[0]
    b = data[1]
    c = data[2]
    print(math. floor(math. sqrt((a * b * 100) / c)))