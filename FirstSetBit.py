def firstsetbit (n):
    position = 1 
    while n > 0:
        if n & 1 == 1:
            return position
        n = n>>1
        position+= 1
    return 0
    
n = int(input("Enter a number: "))
print ("Position of the first set bit is: ",firstsetbit(n))

