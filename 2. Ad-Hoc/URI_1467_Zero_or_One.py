while True:
    try:
        a,b,c = list(map(int,input().split()))
        print("*") if(a == b == c) else print("C") if(a == b) else print("B") if(a == c) else print("A")
    except (EOFError):
        break