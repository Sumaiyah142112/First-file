with open("Python/Update.txt") as file:
    data1= file.read()

with open("Python/Repeated.txt") as file:
    data2 = file.read()


data1 += "\n"
data1 += data2

print("Merging two files....")
with open("Python/Merging.txt","w") as file:
    file.write(data1)