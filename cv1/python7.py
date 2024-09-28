while True:
    try:
        base = int(input("Zadejte základ: "))  
        break  
    except ValueError:
        print("Zadejte platnou číselnou hodnotu (int).") 

while True:
    try:
        exponent = float(input("Zadejte kladný a nenulový mocnitel: "))
        if exponent > 0:
            break
        else:
            print("Mocnitel musí být kladný a nenulový.")
    except ValueError:
        print("Zadejte platnou číselnou hodnotu (float).")

result = 1
for _ in range(int(exponent)):
    result *= base

print(f"Výsledek: {base} na {int(exponent)} je {result}")
