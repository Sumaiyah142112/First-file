def oddOccuring(arr):
    res = 0
    for elemant in arr:
        res = res ^ elemant

    return res  

arr = []

n = int(input("Enter  array size: "))

while(n):
    num = int(input("Enter number: "))
    arr.append(num)
    n-= 1   

print("\nOdd occuring number is: ",oddOccuring(arr))
