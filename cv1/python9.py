stored_pin = "1234"
attempts = 3

while attempts > 0:
    
    entered_pin = input("Give me PIN: ")
    
    if entered_pin == stored_pin:
        print("Succesful login!.")
        break
    else:
       
        attempts -= 1
        if attempts > 0:
            print(f"Wrong PIN. You got {attempts} attempts left.")
        else:
            print("Wrong PIN, You cant try no more.")
