from math import sqrt

while True:
    try:
        L = float(input("Zadej indukcnost [H]: "))
        C = float(input("Zadej kapacitu [F]: "))

        if L <= 0 or C <= 0:
            raise ValueError("Zadejte kladne a nenulove cislo.")

        F = 1 / (2 * 3.14 * sqrt(L * C))
        print("Frekvence je: " + str(F) + "Hz")
        break  
    except ValueError:
        print("Zadejte znovu.")
