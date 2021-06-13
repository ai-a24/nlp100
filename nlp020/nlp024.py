import re
import json

def read_wiki(name):
    with open(name, 'r') as file:
        for line in file:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']

def isFile(string):
    return re.search(r'(ファイル|File):(.+?)\|.+$', string)

def getFileName(string):
    name = re.search(r'(ファイル|File):(.+?)\|.+$', string)
    #name = re.search(r'(ファイル|File):(.*)\|.+$', string) うまく取り出せない
    return name.group(2)

name = 'jawiki-country.json'

text = read_wiki(name).split('\n')

for line in text:
    if isFile(line):
        #print(line)
        print(getFileName(line))
