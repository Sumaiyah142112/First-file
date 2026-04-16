def powerof2(number):
    if (number == 0):
        return False
    if ((number &(~(number-1)))==number):
        return True
    return False

number = int(input("Enter a number: "))

if(powerof2(number)):
    print("\nThe number is a power of 2")
else:
    print("\nThe number is not a power of 2")