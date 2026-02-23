#Read and print OLD content
file = open("Python/Students.txt", "r")
old_content = file.read()
print("Old Content:\n", old_content)
file.close()

#Overwrite the file
file = open("Python/Students.txt", "w")
file.write("My name is Roy. I am a class 8 student and the class monitor.")
file.close()

#Append file
file = open("Python/Students.txt", "a")
file.write("\nMy favourite subject is Science!!")
file.close()

#print NEW content
file = open("Python/Students.txt", "r")
new_content = file.read()
print("\nNew Content:\n", new_content)
file.close()