test = int(input())
dict = {}
while test is not 0:
	test-=1
	prop = int(input())
	if prop in dict:
		dict[prop] += 1
	else:
		dict[prop] =1 
	
dict_to_sort_prepare = dict.keys()
dict_sort = sorted(dict_to_sort_prepare)

for dict_item in dict_sort:
	print('%d aparece %d vez(es)' %(dict_item, dict[dict_item]))