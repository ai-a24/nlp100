"""
f = open("hightemp.txt", 'r')
print(len(f.readlines()))
f.close()
"""
import sys

fp = open(sys.argv[1], 'r')
print(len(fp.readlines()))
fp.close()
