numberLargest = int(input("Enter Larget number: "))
numberSmallest = int(input("Enter Smallest number: "))

while(numberSmallest):
    numberStore = numberSmallest
    numberLargest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is: ", numberLargest)