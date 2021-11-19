for i in range(int(input())):
   m,n = list(map(int, input().split()))
   s=""
   for i in range(m,n+1):
      s += str(m)
      
   print(s + s[::-1])