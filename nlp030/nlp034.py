#名詞の中身を見る
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
list_noun = []
for line in sentences:
    nouns = ""
    cnt= 0
    for morph in line:

        if morph['pos'] == '名詞':
            nouns = "".join([nouns, morph['surface']])
            cnt += 1

        else:
            if cnt >= 2:
                ans.add("".join(nouns))
            nouns = ''
            cnt = 0
        
    if cnt >= 2:
        ans.add("".join(nouns))

#確認用
print('名詞の連接の数:' + str(len(ans)))
for vocab in list(ans)[:10]:
    print(vocab)
