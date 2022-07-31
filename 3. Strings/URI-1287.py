# while True:
#     s = input()
#     a = []
#     flag = True
#     for i in s:
#         if i in "0123456789":
#             a.append(i)
#             print(a)
#         if i == "l":

#             a.append("1")
#             print(a)
#         elif i == 'o' or i == "O":
#             a.append("0")
#             print(a)
#         elif i != ' ' or i != ',':
#             flag = False
#     if(flag):
#         print(a)
#     else:
#         print('error')

while True:
    try:
        s = input()
    except(EOFError):
        break

    s = s.translate(str.maketrans('loO', '100', ' ,'))
    flag = True
    for i in s:
        if i not in '0123456789':
            flag = False
            break
    if(flag):

      
        if(s.count('0') == len(s)):
            print('0')
        else:
            print(s)
    else:
        print('error')
