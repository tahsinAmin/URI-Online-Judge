for i in range(int(input())):
   m, n = map(int, input().split('x'))
   for j in range(5,11):
      if(m==n):
         print("{} x {} = {}".format(m,j,m*j))
      else:
         print("{} x {} = {} && {} x {} = {} ".format(m,j,m*j, n,j,n*j))