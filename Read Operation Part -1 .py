file = open("Python/f1.txt","r")
print(file.read())
file.close()

file = open("Python/f1.txt","r")
print("\n Read in parts \n")
print(file.read())
file.close()

file = open("Python/f1.txt", "a")
file.write("HI! My name is penguin I am 1 year old!")
file.close()
