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

cal1 = list(map(lambda line: line.split('\t')[0], lines))
cal2 = list(map(lambda line: line.split('\t')[1], lines))

re_cal1 = "\n".join(cal1) + "\n"
re_cal2 = "\n".join(cal2) + "\n"
"""
print(re_cal1)
print("\n")
print(re_cal2)
"""
save_file('cal1.txt', re_cal1)
save_file('cal2.txt', re_cal2)
