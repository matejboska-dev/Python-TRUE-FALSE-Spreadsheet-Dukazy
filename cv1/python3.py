while True:
    inp = input("What is your name? ")
    inp2 = input(f"Is your name really {inp}? (yes/no) ")

    if inp2 == "yes":
        print("End of program.")
        break  
    elif inp2 == "no":
        print("Lets try again.")
    else:
        print("Please answer with 'yes' or 'no'.")
