import re
while True:
   mU,mL,mD,mE = [0,0,0,0]
   try:
      o=input()
      if o.isalnum() and (len(o) in range(6,33)):
         for i in o:
            if mU+mL+mD == 3:
               break
            else:
               if i.islower() and mL==0:
                  mL+=1
               if i.isupper() and mU==0:
                  mU+=1
               if i.isdecimal() and mD==0:
                     mD+=1
      else:
         mE+=1

      if(mE==1 or (mU+mL+mD < 3)):
         print("Senha invalida.")
      else:
         print("Senha valida.")

   except(EOFError):
      break