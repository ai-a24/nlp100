import re
import sys

#def read_file(name):

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
    #print(lines)

lines = list(filter(lambda line: line != '', lines))
#print(lines)

#cal1 = list(map(func, lines))

col1 = set(map(lambda line: line.split('\t')[0].strip(), lines))

print("\n".join(col1))
