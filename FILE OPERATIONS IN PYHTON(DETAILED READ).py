file = open("Python/f1.txt","r")
print("Different ways to read a file:")
print("\n Reading using read:")
print(file.read())
file.close()

file = open("Python/f1.txt","r")
print("\n Reading using readline:")
print(file.readline(6))
file.close()

file = open("Python/f1.txt","r")
print("\n Reading using readlines:")
print(file.readlines())
file.close()

file = open("Python/f1.txt","r")
print("\n Reading using for loop:")
for n in file:
    print(n)
file.close()
