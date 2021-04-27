import re

def cipher(string):
    result = ""

    """
    for i, string in enumerate(string):
        print(string[i])
        if string[i].islower():
            result += chr(219 - ord(string[i]))
            
    return result
    """

    for c in string:
        result += chr(219 - ord(c)) if c.islower() else c
    return result    

str1 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

print(str1)

result = cipher(str1)

print(result)
print(cipher(result))
    
