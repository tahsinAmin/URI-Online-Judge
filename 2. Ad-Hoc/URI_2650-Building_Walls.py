m,n = map(int, input().split())

for i in range(m):
   data = input().split()
   if int(data[-1]) > n:
      print(' '.join(data[i] for i in range(len(data)-1)))