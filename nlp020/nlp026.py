import re
import json

def read_wiki(name):
    with open(name, 'r') as file:
        for line in file:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']

def getBasicInfo(string):
    tmp1 = re.search(r'{{基礎情報', string)
    #print(tmp1.end())
    tmp2 = re.search(r'(.*)\n}}\n', string[tmp1.end():])
    return string[tmp1.end():tmp2.end()+1]
    #re.search(r'{{基礎情報', string)

def getTemplate(string):
    name = re.match(r'\|(.+)=(.+)', string)
    if name is None:
        return name
    return '"' + name.group(1) + '"\t"' + name.group(2) + '"'
    #return name.group(1) + name.group(2)

def removeEmp(string):
    #下訂正する必要あり
    name = re.match(r"(.*)('{3,5})(.*?)(\2)(.*)", string)
    if name is None:
        return string
    return name.group(1) + name.group(3) + name.group(5)

name = 'jawiki-country.json'

text = getBasicInfo(read_wiki(name)).split('\n')

print('"フィールド名"\t"値"')

for line in text:
    if getTemplate(line):
        result = getTemplate(line)
        #print(result)
        result = removeEmp(result)
        print(result)
