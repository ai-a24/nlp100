import re
import sys

def read_file(name):
    with open(name, 'r') as file:
        lines = file.read().split("\n")
        return list(filter(lambda line: line != '', lines))

def save_file(name, text):
    with open(name, 'w') as file:
        file.write(text)
"""
def func(line):
    return line.split('\t')[0]
"""        
"""
with open('hightemp.txt', 'r') as file:
    text = re.sub(r'\t', ' ', file.read())
    print(text)
"""

#cal1 = list(map(func, lines))

col1 = read_file('col1.txt')
col2 = read_file('col2.txt')
#print(col1)
#print(col2)

lines = ["{0}\t{1}".format(line1, line2) for line1, line2 in zip(col1, col2)]

result = "\n".join(lines) + "\n"

print(result)
save_file('marge20.txt', result)
