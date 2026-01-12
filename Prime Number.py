#Python program to check if a number is prime
#TAke input from the user
num= int(input("Enter a number:"))
#Check if number is greater than 1 since primes are > than 1
if num > 1:
    #Loop only for square root of num for efficiency
    for i in range(2,int(num**0.5)+1):
        #If numbe ris divisible by any number its not prime
        if num % i == 0:
            print(f"{num} is not a prime number")
            break 
        #If no divisors are fond than the number is prime
        else:
         print(f"{num} is not a prime number")
else:
   #Numbers less than 2 r not prime
   print(f"{num} is not a prime number")     


    