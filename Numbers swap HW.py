x = 5
y = 9
z = 1

if x > y:
    temp = x
    x = y
    y = temp

if x > z:
    temp = x
    x = z
    z = temp

if y > z:
    temp = y
    y = z
    z = temp

print ("x =",x)
print ("y =",y)
print ("z =",z)
