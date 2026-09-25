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
