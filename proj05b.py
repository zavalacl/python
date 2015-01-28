

def open_file():

    while True:
        
        input_file = input("Enter name of input file:")

        try:
            inFile = open(input_file, 'r')
            print("Open successful")
            return inFile

        except FileNotFoundError:
            
            print("Open failed")
        


def process_file(input_file):

    year_input = input("Enter a year:").lower()

    if year_input != "quit":

        region_input = input("Enter a region code:")

        if region_input == "AFR":
            region = "Africa"
            print("Report for",region,"in",year_input,":")

        elif region_input == "AMR":
            region = "Americas"
            print("Report for",region,"in",year_input,":")

        elif region_input == "SEAR":
            region = "South-East Asia"
            print("Report for",region,"in",year_input,":")

        elif region_input == "EUR":
            region = "Europe"
            print("Report for",region,"in",year_input,":")
            
        elif region_input == "EMR":
            region = "Eastern Mediterranean"
            print("Report for",region,"in",year_input,":")

        elif region_input == "WPR":
            region = "Western Pacific"
            print("Report for",region,"in",year_input,":")

        count=0
        pop_count=0
        smallest= 10000000000
        largest = 0
        
        
        for line in input_file:
            line = line.strip()

            year = line[:4]
            region = line[56:60].strip()
            population = int(line[65:71])

            if year_input == year and region_input == region:
                
                count += 1
                pop_count += population

                 
                current_value = int(line[65:71])

                
                if current_value < smallest:
                    smallest = current_value

                if current_value > largest:
                    largest = current_value


        print("Total Entries = ", count)
        print("Total Population = {:#,d}".format(pop_count)) #Didn't print rest of zeros
        print("Average of Total Population =",int(pop_count/count))
        print("Smallest population:",smallest)
        print("Largest population",largest)


    else:
        print("Program halted") 

def main():
    my_file = open_file()
    process_file(my_file)
    my_file.close()


main()


