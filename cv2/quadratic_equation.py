import cmath

try:
    a = float(input("Zadejte hodnotu a: "))
    b = float(input("Zadejte hodnotu b: "))
    c = float(input("Zadejte hodnotu c: "))


    D = (b**2) - (4*a*c)

    if D >= 0:
       
        x1 = (-b - (D**0.5)) / (2*a)
        x2 = (-b + (D**0.5)) / (2*a)
        print("Vypočet korenu v realnych cislech.")
    else:

        x1 = (-b - cmath.sqrt(D)) / (2*a)
        x2 = (-b + cmath.sqrt(D)) / (2*a)
        print("Vypocet korenu v komplexnich cislech.")
except ValueError:
    print("Zadane hodnoty musi byt cisla.")
finally:    
        print(f"X1 = {x1} a X2 = {x2}")