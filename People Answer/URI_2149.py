# É a lista da fib, so que em de ser só soma, intercala soma e multiplicação
def fib(n):
    list_phil = [0, 1]
    a, b = 0, 1
    for i in range(n - 1):
        if i % 2 == 0:  # ‎‎Merges between + and *‎
            a, b = b, a + b
        else:
            a, b = b, a * b
        list_phil.append(a)
    return list_phil[-1]  last value‎


while True:
    try:
        data = int(input())
    except EOFError:
        break
    ‎# If it didn't this would go wrong qnd date was 1, because the initial list of the function starts with 2 values‎
    if data == 1:
        print(0)
    else:
        print(fib(data))