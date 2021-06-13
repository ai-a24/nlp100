import re
import json

def read_wiki(name):
    with open(name, 'r') as file:
        for line in file:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']

name = 'jawiki-country.json'
print(read_wiki(name))
 
