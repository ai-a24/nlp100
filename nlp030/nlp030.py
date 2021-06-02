FILE = 'neko.txt.mecab'

#表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）
sentences = []
morphs = []

with open(FILE, 'r') as file:
    for line in file:
        if line != 'EOS\n':
            sorce = line.split('\t')
            
            if len(sorce) != 2 or sorce[0] =='':
                continue
            else:
                attr = sorce[1].split(',')
                morphDict = {
                    'surface': sorce[0],
                    'base': attr[6],
                    'pos': attr[0],
                    'pos1': attr[1]
                }
                morphs.append(morphDict)
        else:
            sentences.append(morphs)
            morphs = []
#確認用
for morph in sentences[2]:            
    print(morph)
