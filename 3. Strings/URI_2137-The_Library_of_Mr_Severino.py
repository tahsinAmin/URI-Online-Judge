while True:
   try:
      a=[]
      for i in range(int(input())):
         a.append(input())

      a.sorted()
      print(a)
   except(EOFError):
      break
