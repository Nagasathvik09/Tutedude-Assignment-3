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
