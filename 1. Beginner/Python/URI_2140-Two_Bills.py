a = [200, 150, 120, 110, 105, 102, 100, 70, 60, 55, 52, 40, 30, 25, 22, 20, 15, 12, 10, 7,  4]
while True:
    data = input().split()
    if int(data[0]) + int(data[1]) == 0:
        break
    if int(data[1]) - int(data[0]) in a:
        print("possible")
    else:
        print("impossible")


# a=[100,50,20,10,5,2]
# while True:
#     (m, n) = map(int, input().split())
#     bills = 0
#     if m + n == 0:
#         break
#     result = n - m
#     # print ('result is', result,' and bill is',bills)
#     i = 0
#     while result > 1 and i<6:
#         # print('For',a[i])
#         if a[i] <= result:
            
#             if bills == 1 and a[i] == result:
#             	result=0
#             	bills+=1
#             	break
#             if i<5 and (a[i + 1] * 2 == result or a[i] * 2 == result):
#                 # print("Here for",a[i])
#                 result = 0
#                 bills += 2
#                 break
#             else:
#                 result -= a[i]
#                 bills += 1
#             # print ('For',a[i],'result is', result,' and bill is',bills)
#             i -= 1
#         i += 1
        
#     if result == 0 and bills == 2:
#         print('possible')
#     else:
#         print('impossible')