########################
#Computer Project10, money.py
#Algorithm
# Run function init
# Run function str
# Run function repr
# Run function convert
# Run function eq
# Run function ne
# Run function lt
# Run function le
# Run function add
# Run function radd
# Run function sub
# Run function rsub
####################


class Amount (object):
    
    def __init__( self, val=0, code="USD" ):

        #if statement to check if value is not a string
        if val != " ":
            self.__value = val
            
        #otherwise set to default values
        else:
            print("Not an int or float!")
            self.__value = 0

        #if statement to check if code is not correct
        if code != "USD" or code != "CHF" or code != "SEK" or code != "GBP":
            self.__code = code
            
        #otherwise set to default values
        else:
            print("Not a valid code!")
            self.__code = "USD"


    def __str__( self ):
        
        #rounds value to 2 decimal places and displays it
        rounded = round(self.__value,2)
        return str(rounded) + "," + self.__code

    def __repr__( self ):

        #returns self as a string
        return self.__str__() 

    def convert( self, code="USD" ):

        #sets USD to itself
        converted = self.__value

        #if self is a float or int and code is correct, convert values
        if type(self) == float or type(self) == int and code == "USD" or \
           code == "CHF" or code == "SEK" or code == "GBP":
                        
            #converting to USD                            
            if self.__code == "CHF":
                converted = (converted / 0.959220)
            elif self.__code == "SEK":
                converted = (converted / 7.38837)
            elif self.__code == "GBP":
                converted = (converted / 0.638244)

            #converting to whatever           
            if code == "CHF":
                converted = (converted * 0.959220)
                
            elif code == "SEK":
                converted = (converted * 7.38837)

            elif code == "GBP":
                converted = (converted * 0.638244)
                
            return Amount(converted, code)

        #otherwise set to default values
        else:
            print("Not an int or float!")
            self.__value = 0
            self.__code = "USD"
            

    def __eq__( self, other ):

        #calls convert func and converts two values
        selfUSA = self.convert()
        otherUSA = other.convert()

        #sets them equal to eachother and displays if correct
        if selfUSA.__value == otherUSA.__value:
            return True
        return False
        
    def __ne__( self, other ):

        #sets them not equal to eachother and displays if correct
        return not(self == other)

    def __lt__( self, other ):

        #sets them less than one another and displays if correct
        selfUSA = self.convert()
        otherUSA = other.convert()
        if selfUSA.__value < otherUSA.__value:
            return True
        return False

    def __le__( self, other ):

        #sets them less than or equal to one another and displays if correct
        selfUSA = self.convert()
        otherUSA = other.convert()
        if selfUSA.__value <= otherUSA.__value:
            return True
        return False

    def __add__( self, other ):

        #checks if type is an amount, adds if so
        if type(other) == Amount: 
            selfUSA = self.convert()
            otherUSA = other.convert()
            newVal = selfUSA.__value + otherUSA.__value

        #checks if type is a float or int    
        elif type(other) == float or type(other) == int :
            newVal = self.__value + other 
         
        return Amount(newVal, "USD")
               

    def __radd__( self, other ):

        #Add object plus int or float, not object
        A = Amount(other, self.__code)
        return self + A
        

    def __sub__( self, other ):

        #checks if other is an amount, adds both if so
        if type(other) == Amount:
            selfUSA = self.convert()
            otherUSA = other.convert()
            newVal = selfUSA.__value + otherUSA.__value
            
        #checks if other is float or int
        elif type(other) == float or type(other) == int:
            
            newVal = self.__value - other
        
        return Amount(newVal, "USD")

    def __rsub__( self, other ):

        #Subtracts object plus float or int, not object
        A = Amount(other, self.__code) 
        return self - A

