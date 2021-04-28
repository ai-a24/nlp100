import re
import sys

"""
with open('hightemp.txt', 'r') as file:
    text = re.sub(r'\t', ' ', file.read())
    print(text)
"""

with open(sys.argv[1], 'r') as file:
    text = re.sub(r'\t', ' ',file.read())
    print(text)

