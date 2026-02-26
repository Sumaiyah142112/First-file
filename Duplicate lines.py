Output_file= open("Python/Update.txt","w")
Input_file= open("Python/Repeated.txt","r")

lines_seen_so_far = set()#Similar to readlines function
print("Eliminating duplicated lines..")

for line in Input_file:
    if line not in lines_seen_so_far:
        Output_file.write(line)

        lines_seen_so_far.add(line)

Output_file.close()
Input_file.close()
