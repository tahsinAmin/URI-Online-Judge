airports, flights = map(int, input().split())
test = 1
while airports + flights != 0:
    arr = [0]*(airports)
    for _ in range(flights):
        a1, a2 = map(int, input().split())
        arr[a1 - 1] += 1
        arr[a2 - 1] += 1

    max_val = max(arr)
    times = arr.count(max_val)
    start = 0
    print(f"Teste {test}")
    for _ in range(times):
        start = arr.index(max_val, start)
        print(start+1, end=' ')
        start += 1

    print("\n")
    test += 1
    airports, flights = map(int, input().split())
