file1 = open("Python/f1.txt","r")
file2 = open("Python/f2.txt","a")

for line in file1.readlines():
    if not (line.startswith('Coding')):
        print(line)
        file2.write(line)

file2.close()
file1.close()