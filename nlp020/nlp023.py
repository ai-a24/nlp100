import re
import json

def read_wiki(name):
    with open(name, 'r') as file:
        for line in file:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']

def isSection(string):
    return re.match(r'^==*.+==*$', string)
            
def getSectionName(string):
    name = re.match(r'^(==*)(.+?)==*$', string)
        
    return name
    
name = 'jawiki-country.json'

text = read_wiki(name).split('\n')

for line in text:
    if isSection(line):
        name = getSectionName(line)
        print('name:{0}\tlv = {1}'.format(name.group(2), len(name.group(1))-1))
