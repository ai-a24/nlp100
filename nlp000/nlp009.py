import random

str1 = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print(str1)

#print(str.split())

words = str1.split(' ')
result = []

for word in words:
    if 4 < len(word):
        top = word[0]
        #s[-1:] = s[-1:len(s)]
        bot = word[-1:]
        mid = list(word[1:-1])
        random.shuffle(mid)
        result.append(top + "".join(mid) + bot)
    else:
        result.append(word)
        
#print(result)

result2 = " ".join(result)
print(result2)

"""
words = re.findall(r'[a-zA-Z]+', str1)

for

dic = {}
point = [1, 5, 6, 7, 8, 9, 15, 16, 19] 


for i, result in enumerate(result):
    if i + 1 in point:
        dic[result[0:1]] = i + 1
        #dic[i+1] = result[0:1]
    else:
        dic[result[0:2]] = i + 1
        #dic[i+1] = result[0:2]
    
print(dic)

#values = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
#dic = {key: val for key, val in zip(result, values)}
#print(dic)
"""
