import re

str1 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

print(str1)

#print(str.split())

result = re.findall(r'[a-zA-Z]+', str1)

#print(result)

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
