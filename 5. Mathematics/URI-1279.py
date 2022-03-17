trail_space = 0
while True:
    try:
        year = int(input())
    except(EOFError):
        break
    leap, extra_ord = [0, 0]
    if trail_space:
        print("")
    trail_space = 1

    if (((year % 4 == 0) and not(year % 100 == 0)) or (year % 400 == 0)):
        print("This is leap year.")
        leap = 1
        extra_ord = 1
    if(year % 15 == 0):
        print("This is huluculu festival year.")
        extra_ord = 1
    if(year % 55 == 0 and (leap)):
        print("This is bulukulu festival year.")
        extra_ord = 1

    if not(extra_ord):
        print('This is an ordinary year.')

        # how to avoid trail space in 1st and last output
        # Try to prevent using not if possible
