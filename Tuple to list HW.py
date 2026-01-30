student = (" Sumaiyah"," Aleem", " 13 ", "Math")

print("Tuple:",student)

Convert = list(student)

print("List:",Convert)

combined_details = ["".join(map(str, Convert))]
print("Combined list:", combined_details)

str = len(Convert)
print("Sliced",str)
