def temp(x, y, z):
    return x + "時の" + y + "は" + z
    #return "{0}時の{1}は{2}".format(x, y, z)

print("x:")
x = input()

print("y:")
y = input()

print("z:")
z = input()

print(temp(x, y, z))
