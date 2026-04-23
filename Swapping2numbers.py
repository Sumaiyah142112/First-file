def swap1(a,b):

    a = a^b
    b= a^b
    a = a^b
    print("After Swapping: \na = ",a," b =", b)

def swap2(a,b):

    a = (a&b) + (a|b)
    b = a + (~b) + 1
    a = a + (~b) + 1
    print("After Swapping \n    a = ",a," b = ",b)

swap1(15,30)
swap2(15,30)

