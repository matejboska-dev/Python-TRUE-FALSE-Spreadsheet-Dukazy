def calculate_voltage(current, resistance):
    return current * resistance

def calculate_current(voltage, resistance):
    raise NotImplementedError("Výpočet proudu ještě není implementován.")

def calculate_resistance(voltage, current):
    raise NotImplementedError("Výpočet odporu ještě není implementován.")

def get_valid_input():
    while True:
        try:
            answer = int(input("Zadej číslo možnosti: "))
            if answer in [1, 2, 3]:
                return answer
            else:
                print("Prosím zadej číslo 1, 2 nebo 3.")
        except ValueError:
            print("Neplatný vstup! Zadej číslo.")

print("Ahoj!, Vyber jakou veličinu chceš vypočítat")
print("1) Proud")
print("2) Odpor")
print("3) Napětí")

answer = get_valid_input()

if answer == 1:

    voltage = float(input("Zadej napětí (V): "))
    resistance = float(input("Zadej odpor (Ω): "))

    result = calculate_current(voltage, resistance)
    print(f"Proud je {result} A")
    
elif answer == 2:

    voltage = float(input("Zadej napětí (V): "))
    current = float(input("Zadej proud (A): "))

    result = calculate_resistance(voltage, current)
    print(f"Odpor je {result} Ω")

elif answer == 3:

    current = float(input("Zadej proud (A): "))
    resistance = float(input("Zadej odpor (Ω): "))
   
    result = calculate_voltage(current, resistance)
    print(f"Napětí je {result} V")
