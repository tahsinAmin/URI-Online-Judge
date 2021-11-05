min_1, max_1 = map(int, input().split())
result_1 = (min_1*(min_1-1)) // 2
result_2 = (max_1*(max_1+1)) // 2
r = result_2 - result_1
print(r)