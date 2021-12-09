count = 0
while True:
   try:
      n = int(input())
   except(EOFError):
      break
   if n > count:
      count=n
   else:
      break
print(count+1)