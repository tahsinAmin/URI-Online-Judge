while True:
   try:
      d=input()
      s=input()
   except(EOFError):
      break

   if s in d:
      print("Resistente")
   else:
      print("Nao resistente")