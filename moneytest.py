########################
#Computer Project10test.py
#Algorithm
#   import money
#   test, call, and display return output for def str
#   test, call, and display return output for def repr
#   test, call, and display return values for convert function
#   test, call, and display return output for def eq
#   test, call, and display return output for def ne
#   test, call, and display return output for def lt
#   test, call, and display return output for def le
#   test, call, and display return values for def add
#   test, call, and display return values for def radd
#   test, call, and display return values for def sub
#   test, call, and display return values for def rsub
####################

import money

print("Testing def __str__")
print("-" * 20)
A = money.Amount(3.97, "USD")
print(str(A))
print()

print("Testing def __repr__")
print("-" * 20)
A = money.Amount(3.97, "USD")
print(repr(A))
print()

#converting usd to chf
print("Testing def convert for CHF")
print("-" * 30)
A = A.convert("CHF")
print("$3.97 is equal to",A,"Swiss Francs.")
print()

#converting usd to sek
print("Testing def convert for SEK")
print("-" * 30)
A = A.convert("SEK")
print("$3.97 is equal to",A,"Swedish Kronas.")
print()

#converting usd to gbp
print("Testing def convert for GBP")
print("-" * 30)
A = A.convert("GBP")
print("$3.97 is equal to",A,"British Pounds.")
print()

#testing def __eq__ to check if true
print("Testing def __eq__")
print("-" * 20)
A = money.Amount(3.97, "USD")
B = money.Amount(3.97, "USD")
print("$3.97 in USD is equal to $3.97 in USD:",A == B)
print()

#testing def __eq__ to check if false
print("Testing def __eq__")
print("-" * 20)
A = money.Amount(3.97, "USD")
B = money.Amount(3.97, "GBP")
print("$3.97 in USD is equal to $3.97 in GBP:",A == B)
print()

#testing def __ne__ to check if true
print("Testing def __ne__")
print("-" * 20)
A = money.Amount(3.97, "USD")
B = money.Amount(3.97, "GBP")
print("$3.97 in USD is not equal to $3.97 in GBP:",A == B)
print()

#testing def __ne__ to check if false
print("Testing def __ne__")
print("-" * 20)
A = money.Amount(3.97, "USD")
B = money.Amount(3.97, "USD")
print("$3.97 in USD is not equal to $3.97 in USD:",A == B)
print()

#testing def __lt__ to check if true
print("Testing def __lt__")
print("-" * 20)
A = money.Amount(3.97, "USD")
B = money.Amount(3.97, "GBP")
print("$3.97 in USD is less than $3.97 in SEK:",A < B)
print()

#testing def __le__ to check if true
print("Testing def __le__")
print("-" * 20)
A = money.Amount(3.97, "USD")
B = money.Amount(13.97, "GBP")
print("$3.97 in USD is less than or equal to $13.97 in GBP:",A <= B)
print()

#Adding a and b together
print("Testing def __add__")
print("-" * 20)
A = money.Amount(3.97, "USD")
B = money.Amount(3.97, "CHF")
print("$3.97 in USD + $3.97 in CHF is",A + B,"in USD.")
print()

#testing def __radd__
print("Testing def __radd__")
print("-" * 20)
A = money.Amount(3.97, "GBP")
B = 5.0
print("$3.97 in GBP + 5.0 is",A+B,"in USD.")
print()

#Subtracting a and b 
print("Testing def __sub__")
print("-" * 20)
A = money.Amount(3.097, "USD")
B = money.Amount(3.097, "GBP")
print("$3.97 in USD - $3.97 in GBP is",A - B,"in USD.")

#testing def __rsub__
print("Testing def __rsub__")
print("-" * 20)
A = money.Amount(3.097, "USD")
B = 5.0
print("$3.97 in USD - 5.0 is",A - B,"in USD.")
print()







