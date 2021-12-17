m, n = map(int, input().split())
dict={}
for i in range(m):
   k1,k2 = input().split()
   dict[k1],dict[k2] = [k2,k1]

print(dict)
for i in range(n):
   inp = input()
   for j in inp:
      if j in dict:
         print(dict[j],end='')
      else:
         print(j,end='')
   print('')