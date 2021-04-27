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

cal1 = read_file('cal1.txt')
cal2 = read_file('cal2.txt')
#print(cal1)
#print(cal2)

lines = ["{0}\t{1}".format(line1, line2) for line1, line2 in zip(cal1, cal2)]

result = "\n".join(lines) + "\n"

print(result)
save_file('marge.txt', result)
