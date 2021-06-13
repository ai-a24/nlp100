import re
import json

def read_wiki(name):
    with open(name, 'r') as file:
        for line in file:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']

def isCategory(string):
    #return re.search(r'Category:', string)
    return re.search(r'\[\[Category:.+\]\]', string)
    #return re.match(r'^\[\[Category:.+\]\]$', string)
            
name = 'jawiki-country.json'

text = read_wiki(name).split('\n')

for line in text:
    if isCategory(line):
        print(line)

 
