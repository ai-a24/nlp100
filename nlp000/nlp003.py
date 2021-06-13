import re

str1 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

print(str1)

#print(str.split())

result = re.findall(r'[a-zA-Z]+', str1)

#print(result)
str2 = ''

for name in result:
    str2 += str(len(name)) + " " 
    #print(len(name))

print(str2)
