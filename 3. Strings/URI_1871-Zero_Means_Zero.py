while True:
   n1, n2 = list(map(int, input().split()))
   if n1 is 0 and n2 is 0:
      break
   res=str(n1+n2)
   print(res.replace('0',''))