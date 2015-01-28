#########################
#Computer Project 03
#Algorithm
#   prompt for order number
#   prompt for starting number
#   check if inputs are valid
#   count upward
#   if count is bigger than starting num, wrap around
#   if order number reached, add one to count
#   display latin square
#   display closing message
#########################



#Prompt for input,convert to str to int
latin_square_str=input("Input the order of a Latin square:")
latin_square_int=int(latin_square_str)

#Prompt for input, convert str to int
top_left_str=input("Input the top-left number:")
top_left_int=int(top_left_str)

#Check if input is valid
if latin_square_int > 9:
    print("*** Invalid order of square ***")
    print("*** (must be between 1 and 9) ***")

elif top_left_int < 1:
        print("*** Invalid value for top-left number ***")
        print("*** (must be between 1 and 6) ***")
        
#If valid, proceed w/ for loop   
else:

    for A in range (top_left_int, latin_square_int + top_left_int):
        print()
        difference= A - top_left_int
        for B in range (latin_square_int):
            current_num = top_left_int + B + difference
            
            if current_num <= latin_square_int:
                print(current_num, end =' ')
                
            else:
                if current_num % latin_square_int == 0:
                    print(latin_square_int, end=' ')
                else:
                    print(current_num % latin_square_int, end=' ')
            
print()
print() 
print("Program halted.")         





























        
        
    
    
        
    

    
