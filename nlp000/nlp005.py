import re

def n_gram(string, n):
    result = []

    for i in range(len(string) - n + 1):
        result.append(string[i:i+n])

    return result

    #return[string[idx:idx + n] for idx in range(len(string) - n +1)]


str1 = "I am an NLPer"

print(str1)

print(n_gram(str1, 1))
print(n_gram(str1, 2))
print(n_gram(str1, 3))

str2 = re.findall(r'[a-zA-Z]+', str1)

print(n_gram(str2, 1))
print(n_gram(str2, 2))
print(n_gram(str2, 3))

