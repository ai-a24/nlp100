import matplotlib.pyplot as plt
import japanize_matplotlib

from collections import Counter

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
word_cnt = Counter()

for line in sentences:
    for morph in line:
        if morph['pos'] != '記号':
            word_cnt.update([morph['base']])

list_word = word_cnt.most_common()

#確認用
#print('名詞の連接の数:' + str(len(list_word)))
#for vocab in list_word[:10]:
#    print(vocab)

keys = [x[0] for x in list_word[0:10]]
values = [y[1] for y in list_word[0:10]]

fig = plt.figure()
plt.bar(keys, values)
plt.show()

fig.savefig("img036.png")
