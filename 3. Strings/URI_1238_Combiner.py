n = int(input())
while n is not 0:
	n-=1
	str1, str2 = input().split(" ")
	min_length = min(len(str1), len(str2))
	new_str=''
	
	for i in range(min_length):
		new_str+=str1[i] + str2[i]
	
	new_str+= str2[min_length:] if(min_length == len(str1)) else str1[min_length:]
	print(new_str)