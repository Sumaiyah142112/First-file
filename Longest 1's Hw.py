def longest_ones(n):
    count = 0
    
    while n:
        n = n & (n << 1)
        count += 1
    
    return count

num = int(input("Enter your number: "))
print("The longest 1's: ",longest_ones(num))