def calculate_bmi(weight, height):
    
    bmi = weight / (height ** 2)
    return round(bmi, 1)

def bmi_evaluation(bmi):
    
    if bmi < 16.5:
        return "Těžká podvýživa"
    elif 16.5 <= bmi < 18.5:
        return "Podváha"
    elif 18.5 <= bmi < 25:
        return "Normální váha"
    elif 25 <= bmi < 30:
        return "Nadváha"
    elif 30 <= bmi < 35:
        return "Obezita 1. stupně"
    elif 35 <= bmi < 40:
        return "Obezita 2. stupně"
    else:
        return "Obezita 3. stupně"


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Hodnota musí být kladná. Zkuste to znovu.")
            else:
                return value
        except ValueError:
            print("Neplatný vstup. Prosím, zadejte číslo.")

height = get_float_input("Zadejte svou výšku v metrech (např. 1.75): ")
weight = get_float_input("Zadejte svou váhu v kilogramech: ")

bmi = calculate_bmi(weight, height)

print(f"Vaše BMI je: {bmi}")
print(f"Hodnocení vaší váhy: {bmi_evaluation(bmi)}")
