c = 1
while True:
   try:
      m,n=list(map(float, input().split()))
      result = ((n-m)/m)*100
      print("Projeto {}:\nPercentual dos juros da aplicacao: {} %\n".format(c,format(result, ".2f")))
      c+=1

   except(EOFError):
      break