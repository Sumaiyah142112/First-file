with open("Python/f2.txt","a") as file:
    file.write("HI! My name is penguin")
file.close()

with open("Python/f2.txt","r") as file:
    data = file.readlines()
    print("Words in this file are:")
    for lines in data:
        word = lines.split()
        print(word)
file.close()


