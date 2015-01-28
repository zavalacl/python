##################
#Computer Project 05a
#   Algorithm
#       opens population.txt file
#       prompts user to enter a year
#       prompts for output file
#       prints lines containing yr into output file
#       closes population.txt file
##################

#opens population.txt file
input_file = open("population.txt",'r')

#prompts user to enter a year
year_input=input("Enter a year:")

#prompts for output file
output_file = input("Enter name of output file:")

try:
    #write into output file created
    outFile=open(output_file, 'w')
    print("Open successful")

except FileNotFoundError:
    #failure to open output file
    print("Open failed")

      
for line in input_file:
    line = line.strip()
    year = line[:4]

    #if statements to print lines containing year into output file
    if year_input == "all" or year_input == "ALL" or year_input == "":
        print(line,file=outFile)
    elif year_input == year:
        print(line,file=outFile)
    elif year_input == year[:3]:
        print(line,file=outFile)
    elif year_input == year[:2]:
        print(line,file=outFile)
    elif year_input == year[:1]:
        print(line,file=outFile)
        
#closes population.txt           
input_file.close()
