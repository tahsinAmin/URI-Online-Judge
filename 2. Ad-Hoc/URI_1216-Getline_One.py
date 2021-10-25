sum,count= [0,0]
while True:
    try:
       input()
       data = int(input())
    except EOFError:
        break
    sum+=data
    count+=1
print(format(sum/count, ".1f"))