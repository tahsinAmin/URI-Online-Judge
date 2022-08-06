A, B, C = map(float, input().split())

if B > C and (not (A > B)):
    A, B = B, A
elif not (A > C):
    A, C = C, A

for i in range(1):
    if A >= (B + C):
        print("NAO FORMA TRIANGULO")
        break
    if A*A == (B*B + C*C):
        print("TRIANGULO RETANGULO")
    elif A*A > (B*B + C*C):
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    if A == B and B == C:
        print("TRIANGULO EQUILATERO")
        break

    if (B == A) or (A == C) or (C == B):
        print("TRIANGULO ISOSCELES")
