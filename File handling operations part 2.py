file_read = open('Python/Codingal.txt', 'r')
print("File in read Mode")
print(file_read.read())
file_read.close()

file_write = open('Python/Codingal.txt','w')
file_write.write("File in Read Mode.....")
file_write.write("HI!I am penguin.. I am 1 year old")
file_write.close()

file_append = open('Python/Codingal.txt','a')
file_append.write ("/n File in append mode.......")
file_append.write ("HI!I am penguin.. I am 1 year old")
file_append.close()

