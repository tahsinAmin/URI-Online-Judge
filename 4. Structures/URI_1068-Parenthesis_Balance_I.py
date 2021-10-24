while True:
    try:
        data = input()
    except EOFError:
        break
    if data[0] == ")" or data[-1] == "(":
        print("incorrect")
    elif (data.count("(") + data.count(")")) % 2 == 0:
        print("correct")
    else:
        print("incorrect")