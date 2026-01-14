def fibonacci(n):
    if n <= 1:  #Base condition
        return n
    else:
                return fibonacci(n-1) + fibonacci(n-2)
terms= int(input("Enter how many Fibonacci terms u want: "))
print("Fibonacci sequence: ")
for i in range(terms):
       print(fibonacci(i), end='')