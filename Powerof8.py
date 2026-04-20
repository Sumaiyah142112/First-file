def powerof8(n):
    if n<=0:
     return False
    if (n&(n-1))!=0:
       return False
    
    count = 0
    while n>1:
     n>>=1
     count+=1

    return count % 3 ==0

        
n = int(input("Enter a number: "))
if(powerof8(n)):
    print(n ," is a power of 8")
else:
    print(n," is not a power of 8")