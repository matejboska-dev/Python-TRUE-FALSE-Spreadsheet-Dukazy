
raining = False          
windy = False         
fog = False           

if not raining and not windy and not fog:
    print("You dont need an umbrella.")
elif (fog or raining) and not windy:
    print("Take your umbrella with you.")
    
if windy and not raining:
    print("Put some warm headwear on .")
    
if fog:
    print("Put on HiViz waistcoat .")
    
if windy and raining:
    print("Put on waterproof jacket.")
    
if not raining and not fog:
    print("Put your sunglasses on, its nice outside.")
