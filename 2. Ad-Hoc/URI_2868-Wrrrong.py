c = int(input())
for i in range(c):
  num1,op,num2,eq,res = input().split()
  num1,num2,res= int(num1),int(num2),int(res)
  correct = (num1 + num2) if op in '+' else (num1 - num2)  if op in '-' else (num1 * num2)
  dif = 'r' * abs(correct-res)
  print('E{}ou!'.format(dif))