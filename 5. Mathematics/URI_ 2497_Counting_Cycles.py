n = int(input())
count=1
while (n is not -1):
  print('Experiment %d: %d full cycle(s)' %(count, int(n/2)))
  count+=1
  n = int(input())