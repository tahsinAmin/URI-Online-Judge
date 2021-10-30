# https://github.com/Matuiss2/URI-ONLINE/blob/master/1400-%201599/1542.py

while True:
    '''i had q for everything in a variable because of the closing condition
 if i divided into 3 variables before it would give error in the last input'''
    data = list(map(int, input(). split()))
    if data[0] == 0:
        break
    x = int((data[0] * data[1]) / (data[2] - data[0]) * data[2])
    if x == 1:
        print("{} page". format(x)) # print(x, "page") would be faster
    else:
        print("{} pages". format(x))