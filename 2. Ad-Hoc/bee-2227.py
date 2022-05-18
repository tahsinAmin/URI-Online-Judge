# https://www.beecrowd.com.br/judge/en/problems/view/2227

# https://www.youtube.com/watch?v=Hf05vARjcjE

# airports, flights = map(int, input().split())
# arr = [0]*(flights+1)
# for i in range(flights):
#     a1, a2 = map(int, input().split())
#     arr[a1] += 1
#     arr[a2] += 1
# max_val = max(arr)
# index_of_max_val = arr.index(max_val)
# print(index_of_max_val)

airports, flights = map(int, input().split())
cnt = 0
arr = [0]*(flights+1)
a1, a2 = map(int, input().split())
while a1 != a2:
    cnt += 1
    arr[a1] += 1
    arr[a2] += 1
    if cnt == flights:
        # do something
        cnt = 0
    a1, a2 = map(int, input().split())
print("Teste 1")
max_val = max(arr)
start = 0
try:
    while True:
        max_val_index = arr.index(max_val, start)
        start = max_val_index
        print(start, end=' ')
        start += 1
except ValueError:
    print("")
