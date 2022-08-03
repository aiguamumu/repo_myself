import string
import nltk
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
stop_words = stopwords.words("english")
file = open('NLP.txt', encoding='UTF-8')
content = file.read()
#print(type(content))

FromTo=str.maketrans(string.punctuation, " " * len(string.punctuation))
content = content.translate(FromTo)
#由标点到空格的映射替换
word_tokens=wordpunct_tokenize(content)
# 分词
#maketrans（from，to）函数，会输出一个字典，映射表
#string.punctuation即为字符串中的标点符号

filtered_word = [w for w in word_tokens if not w in stop_words]
#去掉停词
new_content=' '.join(filtered_word) # 去掉停词和标点后再次连接
#new_content str类型

token_cixing = nltk.word_tokenize(new_content) #词性标注
tags = nltk.pos_tag(token_cixing)
from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()  # 词形还原

new_part1=new_part2=new_part3=new_part4=''
for each in tags:
    if each[1]=='NN':
        new_part1+=lem.lemmatize(each[0], "n")
        new_part1 +=' '
    if each[1]=='VBZ':
        new_part2+=lem.lemmatize(each[0], "v")
        new_part2 += ' '

    if each[1]=='JJ':
        new_part3+=lem.lemmatize(each[0], "a")
        new_part3 += ' '
    else:
        new_part4+=each[0]
        new_part4+= ' '

new =new_part4 + new_part3 + new_part2 + new_part1
# 词性还原之后的str
new_tokens=wordpunct_tokenize(new)
# 再次分词
print(list(set(new_tokens)))
#去掉相同元素
# 词干提取
# from nltk.stem.porter import PorterStemmer
# stem = PorterStemmer()
#print(stem.stem(word))




