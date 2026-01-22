list = ['Apple','Banana','Guava','Orange','Kiwi']
print("Length of list:", len(list))
print("First Elemant:", list[0])
print("Last Elemant:", list[-1])

list.append('papaya')
print("Updated list:",list)

list.append('Guava')
print("Updated list:",list)

list.sort()
print("Sorted list:",list)

list.pop(1)
print("Updated list:",list)


list.reverse()
print("Reverse list:",list)
print("Multiplication on list:",list*2)

list = list[:4]
print("Sliced list:",list)

list.clear
print("Sliced list:",list)