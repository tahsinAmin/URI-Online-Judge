def is_prime(n):
   if n <= 1:
      return False
   for i in range(2, int(n ** 0.5) + 1):
      if n % i == 0:
         return False
   return True

while True:
    try:
        n = input()
    except(EOFError):
        break
    if is_prime(int(n)):
    	for i in n:
    		if i not in "2357":
    			print("Primo")
    			break
    	else:
    		print("Super")
    else:
    	print("Nada")