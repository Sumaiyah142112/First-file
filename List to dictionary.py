def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result

students = [
    [1, 'Jean Castero', 'V'],
    [2, 'Lula Powell', 'V'],
    [3, 'Lynne Foster', 'V'],
    [4, 'Brian', 'V']
]

print("\nOriginal lists of lists:")
print(students)

print("\nConverted lists of students to dictionary:")
print(test(students))
                                        
    