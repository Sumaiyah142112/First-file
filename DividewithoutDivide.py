def divide(ourDividened,ourDivisor):
    sign = (-1 if((ourDividened<0)^(ourDivisor<0))else 1);

    ourDividened = abs(ourDividened);
    ourDivisor = abs(ourDivisor);
    
    quotientNumber = 0
    tempNumber = 0
    
    #Go from 31 to 0  and accumalate all valid bits
    for i in range(31,-1,-1):
        if (tempNumber +(ourDivisor<<i)<=ourDividened):
            tempNumber += ourDivisor<<i
            quotientNumber |= 1<<i

    if sign ==-1:
        quotientNumber =-quotientNumber
    return quotientNumber

a = int(input("Enter a for a/b: "))
b = int(input("Enter b for a/b: "))
print("Result of ",a,"/",b,"is",divide(a,b))