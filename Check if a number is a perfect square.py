from math import *  
number = input("Enter a number: ")
if number.isalpha():
    print ("Enter a number")
new_number = int(number)
square_root = sqrt(new_number)
if new_number < 0:
    print (new_number)
    print ("Negative numbers are not square numbers")
elif type(square_root) == "int":
    print("The number " + str(new_number) + " is a square number. The square root is " + str(square_root))
else:
    print ("The number " + str(new_number) + " is not a square number.")
    print (square_root)
       
