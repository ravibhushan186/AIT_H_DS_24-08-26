from math import sqrt

a = int(input("Enter the value of a: "))
b = int(input("Entert the value of b: "))
c = int(input("Enter the value of c: "))

# Discriminant
D = b**2 - 4*a*c

if(D > 0):
    r1 = (- b + sqrt(D)) / (2*a)
    r2 = (- b - sqrt(D)) / (2*a)

    print(r1)
    print(r2)
elif D == 0:
    r3 = -b / (2*a)
    print(r3)
else:
    print("No real root")