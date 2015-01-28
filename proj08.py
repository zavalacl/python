#########################################
#Computer Project #08
#Algorithm
#   Run function main
#       run function create_dictionary
#           opens file
#           creates empty dictionary
#           key and values put into tuples
#           assigns key with value
#           closes file and returns dictionary
#       run function population
#           create variables
#           assign population est to current pop
#           finds largest pop and overwrites current pop
#           finds smallest pop and overwrites current pop
#           displays formatted data
#       run function user_input
#           prompts user for state and county
#           creates empty dictionary
#           dictionary searches for state and county
#           if key is not found, raise exception
#           if q or quit is entered, halt program  
########################################


def create_dictionary():
    
    """
    Creates dictionary with items from file.

    Receive:  File to be opened
    Return:   Dictionary with items
    Algorithm:
       opens file
       creates empty dictionary
       ignores header and state column          
       key and values put into tuples
       assigns key with value
       closes file and returns dictionary
       return dictionary
    """

    #tries to open file, otherwise raise exception
    try:
        file = open("CO-EST2013-Alldata.csv", "r", encoding = "ISO-8859-1")
    except FileNotFoundError:
        print("File not found, try again!")
        quit() 
        
    #creates empty dictionary, ignores first line       
    dictionary = {}
    file.readline()

    #strip whitespace and split at commas for each line 
    for line in file:
        line_list = line.strip().split(',')
        #ignores state column
        if line_list[4] != "000":

            #assigns keys to state and county, tuple created  
            key = (line_list[5].lower(), line_list[6].lower()) 

            #assigns val to pop, birth, and net migration, tuple created
            val = (int(line_list[12]),int(line_list[20]),float(line_list[-1]))
            
            #assigns key to that value    
            dictionary[key] = val
    #closes file        
    file.close()
    return (dictionary)
    
        
def population(dictionary):

    """
    Prints smallest and largest populated counties.

    Receive:  Dictionary
    Return:   Smallest and largest county info
    Algorithm:
        create variables
        assign population est to current pop
        finds largest pop and overwrites current pop
        finds smallest pop and overwrites current pop
        displays formatted data
        return formatted display
    """
    
    smallest = 11000000
    largest = 0
    large_key = ()
    small_key = ()
    for key in dictionary:

        #assigns current pop to popest for every key in dictionary
        current_pop = dictionary[key][0]

        #largest value found is set to current pop
        if int(current_pop) > largest:
            largest = current_pop
            large_key = key

        #smallest value found is set to current pop
        if int(current_pop) < smallest:
            smallest = current_pop
            small_key = key

    #prints into columns
    print("County with largest population:")
    print('{:>20s} {:1s} {:<5s}'.format("State name","=",large_key[0]))
    print('{:>20s} {:1s} {:<5s}'.format("County name","=",large_key[1]))
    print('{:>20s} {:1s} {:<5,d}'.format("PopEst","=",dictionary[large_key][0]))
    print('{:>20s} {:1s} {:<5,d}'.format("Births","=",dictionary[large_key][1]))
    print('{:>20s} {:1s} {:.2f}'.format \
          ("NetMigr","=",dictionary[large_key][2]))
    print()

    print("County with smallest population:")
    print('{:>20s} {:1s} {:<5s}'.format("State name","=",small_key[0]))
    print('{:>20s} {:1s} {:<5s}'.format("County name","=",small_key[1]))
    print('{:>20s} {:1s} {:<5,d}'.format("PopEst","=",dictionary[small_key][0]))
    print('{:>20s} {:1s} {:<5,d}'.format("Births","=",dictionary[small_key][1]))
    print('{:>20s} {:1s} {:<.2f}'.format \
          ("NetMigr","=",dictionary[small_key][2]))
    print()


def user_input(dictionary):

    """
    Prints info regarding state and county from user input.

    Receive:  Dictionary
    Return:   Prompted state and county info
    Algorithm:
        prompts user for state and county
        creates empty dictionary
        dictionary searches for state and county
        if key is not found, raise exception
        if q or quit is entered, halt program
        return formatted display
    """

    while True:

        #prompt user for state
        state_input = input("Which state or q/quit to halt:").lower()
        if state_input != "q" and state_input != "quit":

            #prompts user for county
            county_input = input("Which county or q/quit to halt:").lower()
            print()
            
            if county_input != "q" and county_input != "quit":

                try:
                    #assigns key to state and county
                    key = (state_input, county_input)
                    
                    #variable assigns values paired w/keys in dict
                    values = dictionary[key]

                    #prints into columns
                    print('{:>20s} {:1s} {:<5s}'.format \
                          ("State name","=",key[0]))
                    print('{:>20s} {:1s} {:<5s}'.format \
                          ("County name","=",key[1]))
                    print('{:>20s} {:1s} {:<5,d}'.format \
                          ("PopEst","=",values[0]))
                    print('{:>20s} {:1s} {:<5,d}'.format \
                          ("Births","=",values[1]))
                    print('{:>20s} {:1s} {:<.2f}'.format \
                          ("NetMigr","=",values[2]))
                    print()
                    
                #if input entered is not found in dictionary
                except KeyError:
                    print("Key not found!")
                    print() 

            #if q or quit is entered        
            else:
                break
        #if q or quit is entered   
        else:
            break

def main():

    """
    Runs other functions.

    Receive:  n/a
    Return:   processed functions
    Algorithm:
        runs function create_dictionary
        runs function population
        runs function user_input
        closes function main
    """

    #runs func create dictionary
    dictionary = create_dictionary() 
    #passes dict into func population
    population(dictionary)
    #passes dict into func user_input
    user_input(dictionary)
    
main()
    




