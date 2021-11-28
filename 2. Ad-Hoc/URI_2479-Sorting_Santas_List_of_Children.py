a = []
behave,misbehave=[0,0]
for i in range(int(input())):
    op,name=input().split()
    a.append(name)
    behave+= 1 if op == '+' else 0
    misbehave+= 1 if op == '-' else 0
    
print("\n".join(sorted(a)))
print("Se comportaram: {} | Nao se comportaram: {}".format(behave, misbehave))