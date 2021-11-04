target = int(input())
min_1, max_1 = map(int, input().split())
min_2, max_2 = map(int, input().split())
if target in range(min_1, max_1 + 1) and target in range(min_2, max_2 + 1): 
    print("possivel")
else:
    print("impossivel")