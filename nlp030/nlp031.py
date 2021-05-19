FILE = 'neko.txt.mecab'

def read_file():
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

    return sentences

#set型
ans = set()
sentences = read_file()
for line in sentences:
    for morph in line:
        if morph['pos'] == '動詞':
            ans.add(morph['surface']) 

#確認用
print('動詞の表層形の数:' + str(len(ans)))
for vocab in list(ans)[:10]:
    print(vocab)
