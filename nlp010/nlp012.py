import re
import sys

#def read_file(name):

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

with open(sys.argv[1], 'r') as file:
    lines = file.read().split('\n')
    print(lines)

lines = list(filter(lambda line: line != '', lines))
#print(lines)

#cal1 = list(map(func, lines))

col1 = list(map(lambda line: line.split('\t')[0], lines))
col2 = list(map(lambda line: line.split('\t')[1], lines))

re_col1 = "\n".join(col1) + "\n"
re_col2 = "\n".join(col2) + "\n"
"""
print(re_col1)
print("\n")
print(re_col2)
"""
save_file('col1.txt', re_col1)
save_file('col2.txt', re_col2)
