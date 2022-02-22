# while True:
#     try:
#         s1 = input()
#         s2 = input()
#     except(EOFError):
#         break

#     ind = s1[0:2].index(s2)

s1 = input()
s2 = input()


for i in range(len(s1)):
    print(s2.index(s1[i:i+1]))
