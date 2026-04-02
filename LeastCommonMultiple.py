import math
LargestNumber = int(input("Enter Largest number: "))
SmallestNumber = int(input("Enter Smallest number: "))
# Finding LCM using HCF og number
LCM = (LargestNumber* SmallestNumber) // math.gcd(LargestNumber,SmallestNumber)

print("LCM of numbers is: ",LCM)