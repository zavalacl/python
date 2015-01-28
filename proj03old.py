print("At the prompts, please enter the following:\n")
      
print(" Customer's classification code (a character)")
print(" Number of days the vehicle was rented (an integer)")
print(" Odometer reading at the start of the rental period (an integer)")
print(" Odometer reading at the end of the rental period (an integer)\n")

#Prompt for input
code_str = input("Customer code:")


print()

while code_str != 'Q' and code_str != 'q':

    #Prompt for input   
    days_str = input("Number of days:")
    start_str = input("Odometer reading at the start:")
    end_str = input("Odometer reading at the end:")
    print()
    print("Customer summary:")
    
    #Convert strings to integers
    days_int = int (days_str)
    start_int = int( start_str)
    end_int = int (end_str)
    print ("\tclassification code:", code_str)
    
    # If statement if ending odometer reading is smaller
    if start_int < end_int:
        miles_driven = (end_int - start_int) * 1/10
    else:
        miles_driven = ((end_int + 1000000) - start_int) * 1/10

    D_base_charge = 60.00
    B_base_charge = 40.00
    W_base_charge = 190.00
    
    #If statements for Code D
    if code_str == "D" or code_str == "d":
        print("\trental period (days):", days_int)
        print("\todometer reading at start:", start_int)
        print("\todometer reading at end:", end_int)
        print("\tnumber of miles driven:", round(miles_driven, 1))
        if miles_driven >= 100:
            amount_due = (D_base_charge * days_int) + (miles_driven * 0.25)
            print("\tamount due: $", round(amount_due, 2))
            print()
        else:
            print("\tamount due: $", round(D_base_charge * days_int, 2))
            print()            

    #If statements for Code B                
    elif code_str == "B" or code_str == "b":
        print("\trental period (days):", days_int)
        print("\todometer reading at start:", start_int)
        print("\todometer reading at end:", end_int)
        print("\tnumber of miles driven:", round(miles_driven,1))
        amount_due =((B_base_charge * days_int) + (miles_driven * 0.25))
        print("\tamount due: $", round(amount_due, 2))
        print() 

    #If statements for Code W    
    elif code_str == "W" or code_str == "w": 
        print("\trental period (days):", days_int)
        print("\todometer reading at start:", start_int)
        print("\todometer reading at end:", end_int)
        print("\tnumber of miles driven:", round(miles_driven, 1))
        weeks = days_int//7 + 1
        if days_int%7 == 0:
            weeks = days_int//7
        
        if miles_driven/weeks <= 900:
            mileage_charge = W_base_charge * weeks
            print("amount due: $",round(mileage_charge, 2))
            print()
        elif miles_driven/weeks > 900 and miles_driven/weeks <= 1500:
            mileage_charge = W_base_charge 
            base_charge = (100 * weeks)
            amount_due = mileage_charge + base_charge
            print("amount due: $",round(amount_due, 2))
            print()
        elif miles_driven/weeks > 1500:
            mileage_charge = 200 * weeks + (miles_driven - 1500 * weeks) * 0.25
            base_charge = W_base_charge * weeks
            amount_due = base_charge + mileage_charge
            print("amount due: $", round(amount_due, 2))
            print()
            
    else:
        print("\trental period (days):", days_int)
        print("\todometer reading at start:", start_int)
        print("\todometer reading at end:", end_int)
        print("\tnumber of miles driven:", miles_driven)
        print("\tamount due: $",0.00)
        print()
        print("**Invalid classification code**")
        print()
        
    code_str = input("Customer code:")
    print()
    
    
print("Done.")





        








