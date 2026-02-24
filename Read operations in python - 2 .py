file = open("Python/f1.txt","r")
print(file.read())
file.close()

file = open("Python/f1.txt","w")
file.write("File in write mode.....")
file.write("HI! I am penguin. I am 1 year old.")
file.close()

file = open("Python/f1.txt","a")
file.write("\n File in append mode.....")
file.write("HEYYYY!")
file.close()