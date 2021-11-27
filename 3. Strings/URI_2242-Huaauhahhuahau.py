i = input()
v= ['a','e','i','o','u']
vowels=[]
for c in i:
   if c in v:
      vowels.append(c)

if vowels == vowels[::-1]:
   print('S')
else:
   print('N')
