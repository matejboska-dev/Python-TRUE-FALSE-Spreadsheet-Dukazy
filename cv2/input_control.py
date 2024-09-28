while True:
    try:
        x = input("Zadej cislo: ")
        y = int(x) + 1
        print(y)
        break
    except ValueError:
        print("Tohle NENI cislo")
