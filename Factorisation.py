# Factorial of a number using factorisation
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)
    
number = int(input("Enter a number:"))
#Check if number is negative
if number < 0:
    print("Sry, factorial of a negative number does not exist")
elif number==0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of the number is", number,"is",recur_factorial(number))

