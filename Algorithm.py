def one_iteration(a,b):
    return a*b

def multiple_iteration(a,b):
    sum = 0
    for i in range(b):
        sum += a
    return sum

a = int(input("Enter 1st number for multiplication: "))
b = int(input("Enter 2nd number for multiplication: "))

print("One Iteration:",one_iteration(a,b))
print("Multiple Iteration:",multiple_iteration(a,b))
