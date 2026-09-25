# Tutedude-Assignment-3

Task 1: Calculate Factorial Using a Function

CODE

#Calculation of Factorial by using a function
def factorial(number):
    if number == 0:
        return 1
    elif number<0:
        return None
    else:
        return number * factorial(number-1)
num=int(input("Enter the number:"))
result=factorial(num)
if result is None:
    print("Factorial of a negative number is not possible")
else:
    print(f"Factorial of {num} is: {result}")

WORKING

Number is passed as an argument to the function named factorial.
in which we are checking for the possibility for the number , that it might be positive, negative or zero and returning its concerned outputs.

input() is used to take Number input dynamically from the user and after the function call based on the result the concerned output gets printed.

EXAMPLE

If Number is given as 5, then its output will be

Factorial of 5 is: 120


Task 2: Using the Math Module for Calculations

CODE

#Using Math module for calculations
import math
n=float(input("Enter a number: "))
if n<0:
    print("Square root of a negative number is not possible")
    print("Logarithm of a negative number is not possible")
elif n==0:
    print("Square root: ",math.sqrt(n))
    print("Logarithm of 0 is not possible")
    print("Sine: ",math.sin(n))
else:
    print("Square root: ",math.sqrt(n))
    print("Logarithm: ",math.log(n))
    print("Sine: ",math.sin(n))

WORKING

Importing math library by using import keyword, taking input from the user by using input() function and finding out the number's square root, logarithm and its sine value by using math library by checking for the possibility of that number can be negative, positive and zero.

EXAMPLE

If the input n value is given as 25, then

Square root:  5.0

Logarithm:  3.2188758248682006

Sine:  -0.13235175009777303
