def resulting_to_one(n):
   sum = 0
   while n != 0:
      sum += n % 10
      n   =  n // 10
   if sum < 10:
   	return sum
   else:
   	return resulting_to_one(sum)
	
while True:
   n1, n2 = list(map(int, input().split()))
   if n1 is 0 and n2 is 0:
      break

   sum1 = resulting_to_one(n1)
   sum2 = resulting_to_one(n2)
   
   if sum1 is sum2:
   	  print(0)
   elif sum1 > sum2:
      	print(1)
   else:
      	print(2)