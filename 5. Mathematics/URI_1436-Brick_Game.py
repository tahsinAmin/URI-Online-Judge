import math
tests = int(input())
for i in range(tests):
	data = input().split()
	half = math.ceil(int(data[0])/2)
	print("Case {}: {}".format(i+1,data[half]))