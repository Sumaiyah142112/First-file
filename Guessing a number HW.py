import random

# Given list of numbers
numbers = [10, 25, 40, 55, 70, 85, 100]

# Judge randomly selects a number
chosen_number = random.choice(numbers)

print("Welcome to the Quiz Competition!")
print("Guess the number from this list:")
print(numbers)

# User guess
guess = int(input("Enter your guess: "))

# Checking the guess
if guess > chosen_number:
    print("Your guess is higher than the original number.")
elif guess < chosen_number:
    print("Your guess is smaller than the original number.")
else:
    print("Congratulations! You guessed it right!")