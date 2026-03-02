import os
if os.path.exists("Python/R.txt"):
    print("File already exists")
else:
    with open("Python/R.txt","x") as file:
        file.write("apple banana apple mango\n")
        file.write("grapes apple mango\n")
        print("File created")

with open("Python/R.txt", "r") as inputfile:
    words_seen = set()  # does not store duplicates

    with open("Python/U.txt", "w") as outputfile:
        for line in inputfile:
            words = line.split()

            for word in words:
                if word not in words_seen:
                    outputfile.write(word + " ")
                    words_seen.add(word)


print("Duplicate lines removed and written to f.txt")

if os.path.exists("Python/3Hw.txt"):
    os.remove("Python/3Hw.txt")
    print("File deleted.")

if os.path.exists("Python/Folder"):
    os.rmdir("Python/Folder")
    print("Folder removed.")
    


