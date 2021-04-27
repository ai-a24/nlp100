#要復習
import re
import json

import urllib.request
import urllib.parse

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
    ttt = getImageFile(string)
    return string[tmp1.end():tmp2.end()+1]
                  
def getImageFile(string):
    tmp = re.search(r'国旗画像', string)
    print(tmp)
    return tmp

def getImageFileName(article):
    basicInfo = re.search(r'\{\{基礎情報(.+?)\}\}\n', article, re.DOTALL).group(1)
    pat = r'^\|国旗画像\s*=\s*(.+?)\n'
    reg = re.compile(pat, re.MULTILINE | re.DOTALL)
    m = reg.search(basicInfo)
    return m.group(1)
                    

def getImage(finename):
    url = 'https://ja.wikipedia.org/w/api.php?' \
          + 'action=query' \
          + '&format=json' \
          + '&titles=File:' + urllib.parse.quote(finename) \
          + '&prop=imageinfo' \
          + '&iiprop=url'
    with urllib.request.urlopen(url) as res:
        data = json.loads(res.read().decode())
        return data['query']['pages']['-1']['imageinfo'][0]['url']            

def main():
    name = 'jawiki-country.json'
    
    #text = getBasicInfo(read_wiki(name)).split('\n')
    text = getImageFileName(read_wiki(name))
    
    print(getImage(text))
    
            
if __name__== '__main__':
    main()
