# Python program to print a a star pattern
#Get the number of rows form the user
n = int(input("Enter the numbe of rows:"))
#Outer loop for each row
for i in range(1,n+1):
    #INNER LOOP FOR EACH COLUMN IN THE ROW
    for j in range(i):
        #Print star,end with space instead of line
        print("*",end = ' ')
      #After each row print a new line
    print()   