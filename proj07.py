##############################
#Computer Project #7
#
#  Algorithm
#    call function main
#    run function extract
#       read lines 8 and 9 of both files
#       match year with gdp
#       ignore yrs befor 1949
#       ignore second 1969
#    run function processFile
#       create list from text
#       specify 2 term presidents
#    run function figure
#       calculate gdp using previous func
#    function main displays table      
#    close function main
###############################




def extract():

    """
    Extract lines from files and match with year w/ gdp.

    Receive:  The files to be processed
    Return:   join_list with years corresponding their gdp
    Algorithm:
       open file1
       ignore first seven lines
       open file2
       ignore first seven lines
       create empty list
       for loop
          ignore non-digits
          ignore years before 1949 in file1
          ignore 2nd 1969 in file2
          creates tuples within list
          add list to empty list
       return join_list
    """

    #open file 1 and read only lines 8&9
    file1 = open("GDP_Section1All_Hist1.csv", 'r')
    file1.readline()
    file1.readline()
    file1.readline()
    file1.readline()
    file1.readline()
    file1.readline()
    file1.readline()
    #split lines at commas
    line8a =file1.readline().split(",")
    line9a = file1.readline().split(",")
    file1.close()

    #open file 2 and read only lines 8&9 
    file2 = open("GDP_Section1All_Hist2.csv", 'r')
    file2.readline()
    file2.readline()
    file2.readline()
    file2.readline()
    file2.readline()
    file2.readline()
    file2.readline()
    #split lines at commas
    line8b =file2.readline().split(",")
    line9b = file2.readline().split(",")
    file2.close()

    #create empty list
    join_list = list()
    #counting length of tuples
    for i in range(len(line8a)):
        #ignore non-digits and yrs before 1949
        if line8a[i].isdigit() and int(line8a[i]) >= 1949: 
            year = line8a[i]
            gdp = line9a[i]
            #convert yr to int and gdp to float
            i = (int(year),float(gdp))
            #add to empty list
            join_list.append(i)
        
    #counting length of tuples
    for i in range(len(line9a)):
        #ignore second 1969 tuple
        if line8b[i].isdigit() and line8b[i] != "1969":
            year = line8b[i]
            gdp = line9b[i]
            #convert yr to int and gdp to float
            i = (int(year),float(gdp))
            #add to empty list
            join_list.append(i)       
    #return combined lists extracted from both files            
    return join_list
    

def processFile():

    """
    Creating list from file while fixing certain issues

    Receive:  The file to be processed
    Return:   president_list with fixed solutions
    Algorithm:
       open file3
       create empty list
       for loop
          strip whitespace
          split at commas
          separate first and last name
          ignore first name
          list years and convert to int
        if loop
          if length of year list is more than 4
             add 1 and 2 to presidents last name if served two terms
             add to empty list
          else display regular tuple and add to empty list
       return president_list
    """
    #open file 3
    file3 = open("the_correct_presidents.txt", 'r')

    #create empty list
    president_list = list()
    file3.readline()
    
    #for each line in file 3
    for line in file3:

        #strip whitespace and split at commas
        info = line.strip().split(",")

        #targets first position in tuple(president's name)
        name = info[0]

        #splits first and last name
        name = name.split()

        #targets last name only
        last_name = name[-1]

        #targets years in tuple of list and splits at dash
        years = info[-2].split('-')

        #range of years starting from 1st yr to last yr and converts to int
        last_years = list(range(int(years[0]), int(years[1])))

        #if length of tuple in list is equal to 8(2 terms)
        if len(last_years) == 8:

            #add '1' to last name for first term and add to empty list
            tup = (last_name+'1', last_years[0:4], info[-1])
            president_list.append(tup)

            #add '2' to last name for second term and add to empty list
            tup = (last_name+'2', last_years[4:], info[-1])
            president_list.append(tup)
        
        else:
            #add last name, years, and party to empty list
            tup = (last_name, last_years, info[-1])
            president_list.append(tup)
            
    # return lists of president info           
    return president_list


def figure(join_list,president_list):

    """
    Calculate gdp and format table.

    Receive:  join_list and president_list
    Return:   table with president info and gdp avg
    Algorithm:
       call join_list and president_list
       set count equal to zero
       for loop in range of join_list
          i is set to second index in tuple of index
          add gdps and calculate average
       return average
    """
    #set count 
    count =  0
    #in range of join_list
    for i in range(join_list):

        #target gdp value
        i = (join_list[0][1])

        #add gdp values
        i += 1

        #calculate average
        average = i/4

        #add one to count
        count += 1
        
    #return calculated avg
    return average

def main(figure):
    
    """
    Call function figure.

    Receive:  Function figure w/ join_list and president_list passed
    Return:   Formatted table
    Algorithm:
       Run function figure
          Display formatted table         
       Close function main
    """
    

main.close(figure) 
    
    

    

    
    

    

    


 







   


