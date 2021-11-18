import re
while True:
   try:
      takeOut=input()
      s=input()
      l1 = len(s)
      s = re.sub(("["+takeOut+"]"), '', s)
      print(l1-len(s))
   
   except(EOFError):
      break