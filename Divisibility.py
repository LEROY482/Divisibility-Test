#Python program checks whether the given number is divisible by both 2 and 5 using If Else.

number = int(input(" Enter any +ve Integer : "))

if((number % 2 == 0) and (number % 5 == 0)):
    print("Given Number {0} is Divisible by 2 and 5".format(number))
else:
    print("Given Number {0} is Not Divisible by 2 and 5".format(number))
