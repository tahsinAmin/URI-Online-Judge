while(True):
  try:
    n = int(input())
    height = n//2 + 1
    
    asterik = 1
    h = height - 1
    for i in range(height):

    	for j in range(h+asterik):	
    			print(" ",end="") if (j < h) else print("*",end="")
    			
    	asterik += 2
    	h-=1
    	print("")

    asterik = 1
    h = height-1
    for i in range(2):

      for j in range(h+asterik):	
          print(" ",end="") if (j < h) else print("*",end="")
          
      asterik += 2
      h-=1
      print("")

    print("")
  except(EOFError):
    break