A, B, C = map(float, input().split())

if ((A + B) > C and (B + C) > A and (C + A) > B):
    print(f"Perimetro = {round((A + B + C),1)}")
else:
    print(f"Area = {round((0.5 * (A + B) * C),1)}")
