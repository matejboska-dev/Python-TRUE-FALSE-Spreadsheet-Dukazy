import datetime

while True:
    try:
        day = int(input("Zadejte den narození: "))
        month = int(input("Zadejte měsíc narození: "))
        year = int(input("Zadejte rok narození: "))

        start_date = datetime.date(year, month, day)
        print(f"Datum vašeho narození je {start_date}")
        break
    except ValueError:
        print("Nevalidní datum, zkuste to prosím znovu.")
