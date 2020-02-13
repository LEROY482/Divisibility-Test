#Python program checks whether the given number is divisible by both 2 and 5 using If Else.

number = int(input(" Enter any +ve Integer : ")) #DATA IS BEING INPUTED BY THE USER #iNT MAKES SURE THE NUMBER IS AN INTERGER.

if((number % 2 == 0) and (number % 5 == 0)): # % STANDS FOR CHECKING FOR THE REMAINDER.
    print("Given Number {0} is Divisible by 2 and 5".format(number)) # If the remaider is more than 0 it is divisible by 2 or 5
else:
    print("Given Number {0} is Not Divisible by 2 and 5".format(number))
