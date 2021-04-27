import re
import sys
import collections
from collections import Counter

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

lines = list(map(lambda line: line.split('\t'), lines))

#print(lines)
cal1 = list(map(lambda line: line[0].strip(), lines))

#print(Counter(cal1).most_common())

result = list(map(lambda x: f"{x[0]}\t{x[1]}", Counter(cal1).most_common()))

print("\n".join(result)) 
