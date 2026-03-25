def myfunction1(n):
    if(n <= 0):
        return
    for i in range (0,n+1):
        print("Codingal")
    myfunction1(n/2)
    myfunction1(n/3)
print("Recurrence: T(n) = T(n/2) + T(n/3) + O(n)")
print("Time Complexity: O(n)\n")
def myfunction2(n):
    if(n<=1):
        return
    print("Codingal")
    myfunction2(n-1)
print("Recurrence: T(n) = T(n-1) + O(1) ")
print("Time Complexity: O(n)")
