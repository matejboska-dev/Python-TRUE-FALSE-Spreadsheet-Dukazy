import datetime

def check_year(year):
    current_year = datetime.datetime.now().year
    if year < (current_year - 119) or year > current_year:
        raise Exception("Rok musi byt mezi {} a {}.".format(current_year - 119, current_year))
    
def check_month(month):
    if month < 1 or month > 12:
        raise Exception("Mesic musi byt cislo od 1 do 12.")

def check_day(day, month):
    days_in_month = {
        1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31, 
        2: 29,  
        4: 30, 6: 30, 9: 30, 11: 30  
    }
    if day < 1 or day > days_in_month.get(month, 0):
        raise Exception(f"Den pro mesic {month} musi byt mezi 1 a {days_in_month[month]}.")
    
def check_summer_holidays(month):
    if month == 7 or month == 8:
        raise Exception("Datum narozeni nesmi spadat do letních prázdnin (červenec, srpen).")

try:
    year = int(input("Zadejte rok narozeni: "))
    check_year(year)
    
    month = int(input("Zadejte mesic narození (1-12): "))
    check_month(month)
    
    day = int(input("Zadejte den narozeni: "))
    check_day(day, month)
    
    check_summer_holidays(month)
    
    print("Datum narození je platné.")
    
except Exception as e:
    print(f"Chyba: {e}")
