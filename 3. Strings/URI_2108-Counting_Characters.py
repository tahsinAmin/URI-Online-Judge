highest = 0
biggest_word = ""

while True:
    data = input().split()
    size = []
    if data[0] == "0":
        break
    for i in data:
        size.append(len(i)) 
        if len(i) >= highest: 
            highest = len(i)
            biggest_word = i
    print("-".join(map(str,size)))
print()
print("The biggest word:", biggest_word)