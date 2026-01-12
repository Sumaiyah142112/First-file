num= int(input("Enter a number:"))
digits =str(num)
abs= len(digits)
armstrong_sum = sum(int(d)**abs for d in digits)
if armstrong_sum == num:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")