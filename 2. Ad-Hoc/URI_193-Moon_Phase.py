m,n = list(map(int, input().split()))
if m > n and n in range(3,97):
   print("minguante")
elif n in range(0,3):
   print("nova")
elif n in range(3,97):
   print("crescente")
elif n in range(97,101):
   print("cheia")