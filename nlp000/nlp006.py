import re

def n_gram(string, n):
    result = []

    for i in range(len(string) - n + 1):
        result.append(string[i:i+n])

    return result

    #return[string[idx:idx + n] for idx in range(len(string) - n +1)]


str1 = "paraparaparadise"
str2 = "paragraph"

print(str1)
print(str2)

print(n_gram(str1, 2))
print(n_gram(str2, 2))

x_set = set(n_gram(str1, 2))
y_set = set(n_gram(str2, 2))

print(x_set | y_set)
#print(x_set.union(y_set))

print(x_set & y_set)
#print(x_set.intersection(y_set))

print(x_set - y_set)
#print(x_set.difference(y_set))
print(y_set - x_set)

print('se' in x_set)
print('se' in y_set)

