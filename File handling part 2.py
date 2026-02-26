new_file = open("file.txt","x")
new_file.close()

import os
print("Checking if my file exists or not....")
if os.path.exists("Python/f3.txt"):
    os.remove("Python/f3.txt")
else:
    print("File does not exist")

file = open("Python/1.txt","w")
file.write("Hi! I am penguin i am 1 year old")
file.close()

os.remove("Python/Codingal.txt")
os.rmdir("Python/Folder")