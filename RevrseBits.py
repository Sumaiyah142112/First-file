def ReverseBits(n):
    res = 0
    while n > 0:
        bit = n & 1
        res = res<<1
        res = res|bit
        n = n >> 1
    return res

num = int(input("Enter a number: "))
print("Reversed number: ",ReverseBits(num))