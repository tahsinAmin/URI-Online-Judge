n = int(input())

for i in range(n):
	s = input()
	s_len = len(s)
	back_counter = int(input())
	new_s = ''
	
	for j in range(s_len):
		order_value = ord(s[j]) - back_counter
		order_value = (90 - (65-order_value) + 1) if order_value < 65 else order_value
		new_s+= chr(order_value)

	print(new_s)