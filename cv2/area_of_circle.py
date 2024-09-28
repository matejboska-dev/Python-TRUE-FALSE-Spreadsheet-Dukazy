import math

r = int(input("Zadejte polomer kruhu: "))

s_kruhu = math.pi * r**2

if r <= 0:
    raise ArithmeticError
else:
    print(f"Obsah kruhu je: {s_kruhu}")