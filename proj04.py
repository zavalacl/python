########################
#Computer Project #04
#Algorithm
#   prompt yes/no for input if resident
#   perform while loop statement
#   prompt user for level and credit
#   only prompt user for college if upperclassmen level
#   perform calculation
#   display total cost
#   prompt user yes/no to perform another calculation
#   halt program if user enters "no"
########################


print("Tuition Calculator \n")
#tuition costs
lower_class_res = 440.00
upper_class_res = 490.25
lower_class_non_res = 1165.50
upper_class_non_res = 1202.25
grad_class_res = 646.00
grad_class_non_res = 1269.00
#special fees
bus_fee_part = 100.00
bus_fee_full = 200.00
eng_fee_part = 361.00
eng_fee_full = 590.00
hea_fee_part = 50.00
hea_fee_full = 100.00
sci_fee_part = 50.00
sci_fee_full = 100.00
grad_fee_part = 37.50
grad_fee_full = 75.00
#tax fees
ASMSU_tax = 18.00
COGS_tax = 9.25
FM_radio_tax = 3.00
state_news_tax = 5.00


#prompt user input
resident = input("Resident (Yes/No):").lower()

#if resident perform this while block
while resident == "yes":
    
    level_input = "freshman", "sophomore", "junior", "senior", "graduate"
    level_input=input("Input level - freshman, sophomore, junior, senior," \
                      " graduate:").lower()

    if level_input == "freshman" or level_input == "sophomore":
        
        credit_input_str=input("Input credits this semester:")
        credit_input_int=int(credit_input_str)

        if credit_input_int >= 6:
        
            tuition = (lower_class_res * credit_input_int)
            fees = (ASMSU_tax + FM_radio_tax + state_news_tax)
            total = (tuition + fees)
            print("Total bill: ${:#,.2f}".format(total))

        else:
            tuition = (lower_class_res * credit_input_int)
            fees = (ASMSU_tax + FM_radio_tax)
            total = (tuition + fees)
            print("Total bill: ${:#,.2f}".format(total))

    elif level_input == "junior" or level_input == "senior":
        
        #college input only for upperclassmen
        college_input=input("College - business, engineering, health,"\
                            " science, none:").lower()

        if college_input == "business":
            
            credit_input_str=input("Input credits this semester:")
            credit_input_int=int(credit_input_str)
            
            if credit_input_int >= 6:
            
                tuition = (upper_class_res * credit_input_int)
                fees = (ASMSU_tax + FM_radio_tax + state_news_tax \
                        + bus_fee_full)
                total = (tuition + fees)
                print("Total bill: ${:#,.2f}".format(total))

            else:
                tuition = (upper_class_res * credit_input_int)
                fees = (ASMSU_tax + FM_radio_tax + bus_fee_part)
                total = (tuition + fees)
                print("Total bill: ${:#,.2f}".format(total))

        elif college_input == "engineering":
            
            credit_input_str=input("Input credits this semester:")
            credit_input_int=int(credit_input_str)
            
            if credit_input_int >= 6:
            
                tuition = (upper_class_res * credit_input_int)
                fees = (ASMSU_tax + FM_radio_tax + state_news_tax \
                        + eng_fee_full)
                total = (tuition + fees)
                print("Total bill: ${:#,.2f}".format(total))

            else:
                tuition = (upper_class_res * credit_input_int)
                fees = (ASMSU_tax + FM_radio_tax + eng_fee_part)
                total = (tuition + fees)
                print("Total bill: ${:#,.2f}".format(total))

        elif college_input == "health":
            
            credit_input_str=input("Input credits this semester:")
            credit_input_int=int(credit_input_str)
            
            if credit_input_int >= 6:
            
                tuition = (upper_class_res * credit_input_int)
                fees = (ASMSU_tax + FM_radio_tax + state_news_tax \
                        + hea_fee_full)
                total = (tuition + fees)
                print("Total bill: ${:#,.2f}".format(total))

            else:
                tuition = (upper_class_res * credit_input_int)
                fees = (ASMSU_tax + FM_radio_tax + hea_fee_part)
                total = (tuition + fees)
                print("Total bill: ${:#,.2f}".format(total))

        elif college_input == "science":
            
            credit_input_str=input("Input credits this semester:")
            credit_input_int=int(credit_input_str)
            
            if credit_input_int >= 6:
            
                tuition = (upper_class_res * credit_input_int)
                fees = (ASMSU_tax + FM_radio_tax + state_news_tax \
                        + sci_fee_full)
                total = (tuition + fees)
                print("Total bill: ${:#,.2f}".format(total))

            else:
                tuition = (upper_class_res * credit_input_int)
                fees = (ASMSU_tax + FM_radio_tax + sci_fee_part)
                total = (tuition + fees)
                print("Total bill: ${:#,.2f}".format(total))
                
    #else statement made for graduate students              
    else:
       
        college_input=input("College - business, engineering, health," \
                            " science, none:").lower()

        if level_input == "graduate":

            if college_input == "engineering":
                
                credit_input_str=input("Input credits this semester:")
                credit_input_int=int(credit_input_str)

                if credit_input_int >= 6:
                
                    tuition = (grad_class_res * credit_input_int)
                    fees = (COGS_tax + FM_radio_tax + state_news_tax \
                            + grad_fee_full + eng_fee_full)
                    total = (tuition + fees)
                    print("Total bill: ${:#,.2f}".format(total))

                else:
                    tuition = (grad_class_res * credit_input_int)
                    fees = (COGS_tax + FM_radio_tax + grad_fee_part \
                            + eng_fee_part)
                    total = (tuition + fees)
                    print("Total bill: ${:#,.2f}".format(total))
                    
            elif college_input == "business":

                credit_input_str=input("Input credits this semester:")
                credit_input_int=int(credit_input_str)

                if credit_input_int >= 6:
                
                    tuition = (grad_class_res * credit_input_int)
                    fees = (COGS_tax + FM_radio_tax + state_news_tax \
                            + bus_fee_full)
                    total = (tuition + fees)
                    print("Total bill: ${:#,.2f}".format(total))

                else:
                    tuition = (grad_class_res * credit_input_int)
                    fees = (COGS_tax + FM_radio_tax + bus_fee_part)
                    total = (tuition + fees)
                    print("Total bill: ${:#,.2f}".format(total))

            elif college_input == "health":
            
                credit_input_str=input("Input credits this semester:")
                credit_input_int=int(credit_input_str)
                
                if credit_input_int >= 6:
                
                    tuition = (grad_class_res * credit_input_int)
                    fees = (COGS_tax + FM_radio_tax + state_news_tax \
                            + hea_fee_full)
                    total = (tuition + fees)
                    print("Total bill: ${:#,.2f}".format(total))

                else:
                    tuition = (grad_class_res * credit_input_int)
                    fees = (COGS_tax + FM_radio_tax + hea_fee_part)
                    total = (tuition + fees)
                    print("Total bill: ${:#,.2f}".format(total))

            elif college_input == "science":
            
                credit_input_str=input("Input credits this semester:")
                credit_input_int=int(credit_input_str)
                
                if credit_input_int >= 6:
                
                    tuition = (grad_class_res * credit_input_int)
                    fees = (COGS_tax + FM_radio_tax + sci_fee_full \
                            +state_news_tax)
                    total = (tuition + fees)
                    print("Total bill: ${:#,.2f}".format(total))

                else:
                    tuition = (grad_class_res * credit_input_int)
                    fees = (COGS_tax + FM_radio_tax + sci_fee_part)
                    total = (tuition + fees)
                    print("Total bill: ${:#,.2f}".format(total))

            elif college_input == "none":
                
                credit_input_str=input("Input credits this semester:")
                credit_input_int=int(credit_input_str)
                
                if credit_input_int >= 6:
                    tuition = (grad_class_res * credit_input_int)
                    fees = (COGS_tax + FM_radio_tax + grad_fee_full \
                            + state_news_tax)
                    total = (tuition + fees)
                    print("Total bill: ${:#,.2f}".format(total))

                else:
                    tuition = (grad_class_res * credit_input_int)
                    fees = (COGS_tax + FM_radio_tax + grad_fee_part)
                    total = (tuition + fees)
                    print("Total bill: ${:#,.2f}".format(total))

    #prompt user for another calculation                
    again=input("Do you want to calculate again (Yes/No): ").lower()
    print()
    if again == "no":
        break 
    elif again == "yes":
        resident = input("Resident (Yes/No):").lower()
        

#if NOT resident perform this while block
while resident == "no": 
        
    level_input = "freshman", "sophomore", "junior", "senior", "graduate"
    level_input=input("Input level - freshman, sophomore, junior, senior," \
                      " graduate:").lower()

    if level_input == "freshman" or level_input == "sophomore":
        
        credit_input_str=input("Input credits this semester:")
        credit_input_int=int(credit_input_str)

        if credit_input_int >= 6:
        
            tuition = (lower_class_non_res * credit_input_int)
            fees = (ASMSU_tax + FM_radio_tax + state_news_tax)
            total = (tuition + fees)
            print("Total bill: ${:#,.2f}".format(total))

        else:
            tuition = (lower_class_non_res * credit_input_int)
            fees = (ASMSU_tax + FM_radio_tax)
            total = (tuition + fees)
            print("Total bill: ${:#,.2f}".format(total))

    elif level_input == "junior" or level_input == "senior":
        
        #college input only for upperclassmen                
        college_input=input("College - business, engineering, health," \
                            "science, none:").lower()

        if college_input == "business":

            credit_input_str=input("Input credits this semester:")
            credit_input_int=int(credit_input_str)

            if credit_input_int >= 6:
            
                tuition = (upper_class_non_res * credit_input_int)
                fees = (ASMSU_tax + FM_radio_tax + state_news_tax + \
                        bus_fee_full)
                total = (tuition + fees)
                print("Total bill: ${:#,.2f}".format(total))

            else:
                tuition = (upper_class_non_res * credit_input_int)
                fees = (ASMSU_tax + FM_radio_tax + bus_fee_part)
                total = (tuition + fees)
                print("Total bill: ${:#,.2f}".format(total))

        elif college_input == "engineering":
            
            credit_input_str=input("Input credits this semester:")
            credit_input_int=int(credit_input_str)
            
            if credit_input_int >= 6:
            
                tuition = (upper_class_non_res * credit_input_int)
                fees = (ASMSU_tax + FM_radio_tax + state_news_tax + \
                        eng_fee_full)
                total = (tuition + fees)
                print("Total bill: ${:#,.2f}".format(total))

            else:
                tuition = (upper_class_non_res * credit_input_int)
                fees = (ASMSU_tax + FM_radio_tax + eng_fee_part)
                total = (tuition + fees)
                print("Total bill: ${:#,.2f}".format(total))

        elif college_input == "health":
            
            credit_input_str=input("Input credits this semester:")
            credit_input_int=int(credit_input_str)
            
            if credit_input_int >= 6:
            
                tuition = (upper_class_non_res * credit_input_int)
                fees = (ASMSU_tax + FM_radio_tax + state_news_tax \
                        + hea_fee_full)
                total = (tuition + fees)
                print("Total bill: ${:#,.2f}".format(total))

            else:
                tuition = (upper_class_non_res * credit_input_int)
                fees = (ASMSU_tax + FM_radio_tax + hea_fee_part)
                total = (tuition + fees)
                print("Total bill: ${:#,.2f}".format(total))

        elif college_input == "science":
            
            credit_input_str=input("Input credits this semester:")
            credit_input_int=int(credit_input_str)
            
            if credit_input_int >= 6:
            
                tuition = (upper_class_non_res * credit_input_int)
                fees = (ASMSU_tax + FM_radio_tax + state_news_tax \
                        + sci_fee_full)
                total = (tuition + fees)
                print("Total bill: ${:#,.2f}".format(total))

            else:
                tuition = (upper_class_non_res * credit_input_int)
                fees = (ASMSU_tax + FM_radio_tax + sci_fee_part)
                total = (tuition + fees)
                print("Total bill: ${:#,.2f}".format(total))
                
    #else statement made for graduate engineering students                              
    else:
       
        college_input=input("College - business, engineering, health," \
                            " science, none:").lower()

        if level_input == "graduate":

            if college_input == "engineering":
                
                credit_input_str=input("Input credits this semester:")
                credit_input_int=int(credit_input_str)

                if credit_input_int >= 6:
                
                    tuition = (grad_class_non_res * credit_input_int)
                    fees = (COGS_tax + FM_radio_tax + state_news_tax \
                            + grad_fee_full + eng_fee_full)
                    total = (tuition + fees)
                    print("Total bill: ${:#,.2f}".format(total))

                else:
                    tuition = (grad_class_non_res * credit_input_int)
                    fees = (COGS_tax + FM_radio_tax + grad_fee_part \
                            + eng_fee_part)
                    total = (tuition + fees)
                    print("Total bill: ${:#,.2f}".format(total))
                    
            elif college_input == "business":

                credit_input_str=input("Input credits this semester:")
                credit_input_int=int(credit_input_str)

                if credit_input_int >= 6:
                
                    tuition = (grad_class_non_res * credit_input_int)
                    fees = (COGS_tax + FM_radio_tax + state_news_tax \
                            +bus_fee_full)
                    total = (tuition + fees)
                    print("Total bill: ${:#,.2f}".format(total))

                else:
                    tuition = (grad_class_non_res * credit_input_int)
                    fees = (COGS_tax + FM_radio_tax + bus_fee_part)
                    total = (tuition + fees)
                    print("Total bill: ${:#,.2f}".format(total))

            elif college_input == "health":
            
                credit_input_str=input("Input credits this semester:")
                credit_input_int=int(credit_input_str)
                
                if credit_input_int >= 6:
                
                    tuition = (grad_class_non_res * credit_input_int)
                    fees = (COGS_tax + FM_radio_tax + state_news_tax \
                            +hea_fee_full)
                    total = (tuition + fees)
                    print("Total bill: ${:#,.2f}".format(total))

                else:
                    tuition = (grad_class_non_res * credit_input_int)
                    fees = (COGS_tax + FM_radio_tax + hea_fee_part)
                    total = (tuition + fees)
                    print("Total bill: ${:#,.2f}".format(total))

            elif college_input == "science":
            
                credit_input_str=input("Input credits this semester:")
                credit_input_int=int(credit_input_str)
                
                if credit_input_int >= 6:
                
                    tuition = (grad_class_non_res * credit_input_int)
                    fees = (COGS_tax + FM_radio_tax + sci_fee_full \
                            +state_news_tax)
                    total = (tuition + fees)
                    print("Total bill: ${:#,.2f}".format(total))

                else:
                    tuition = (grad_class_non_res * credit_input_int)
                    fees = (COGS_tax + FM_radio_tax + sci_fee_part)
                    total = (tuition + fees)
                    print("Total bill: ${:#,.2f}".format(total))

            elif college_input == "none":
                
                credit_input_str=input("Input credits this semester:")
                credit_input_int=int(credit_input_str)
                
                if credit_input_int >= 6:
                    tuition = (grad_class_non_res * credit_input_int)
                    fees = (COGS_tax + FM_radio_tax + grad_fee_full \
                            +state_news_tax)
                    total = (tuition + fees)
                    print("Total bill: ${:#,.2f}".format(total))

                else:
                    tuition = (grad_class_non_res * credit_input_int)
                    fees = (COGS_tax + FM_radio_tax + grad_fee_part)
                    total = (tuition + fees)
                    print("Total bill: ${:#,.2f}".format(total))
                        
    #prompt user for another calculation                
    again=input("Do you want to calculate again (Yes/No): ").lower()
    print()
    if again == "no":
        break 
    elif again == "yes":
        resident = input("Resident (Yes/No):").lower()




