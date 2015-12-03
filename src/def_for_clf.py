'''所有需要用到的函数都放在了这里'''


import re
from scipy.sparse import coo_matrix
import numpy as np
import jieba
from scipy.sparse.csr import csr_matrix
import xml.dom.minidom
from scipy.sparse.csc import csc_matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import SelectKBest,chi2
from scipy.sparse import hstack


import sys, os
ROOTDIR = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.append(os.path.join(ROOTDIR, "lib"))
# Set your own model path
MODELDIR=os.path.join('/home/fish/', "ltp_data")
from pyltp import Segmentor,Postagger,NamedEntityRecognizer  # @UnresolvedImport

#分词功能 
segmentor = Segmentor()
segmentor.load(os.path.join(MODELDIR, "cws.model"))
postagger = Postagger()
postagger.load(os.path.join(MODELDIR, "pos.model"))
recognizer = NamedEntityRecognizer()
recognizer.load(os.path.join(MODELDIR, "ner.model"))


def ltp(sentence):
    words = segmentor.segment(sentence)
    #词性标注功能 
    postags = postagger.postag(words)
    #实体识别 
    netags = recognizer.recognize(words, postags)
    l = []
    li = zip(list(words),list(postags),list(netags))
    for a,b,c in li:
# 去掉命名实体
        if c == 'O':
#             去掉所有名词
#             if not re.search('n',b):
            l.append(a)
#     print(l)
    return l

def ltp_p(sentence):
    words = segmentor.segment(sentence)

    return list(words)

# 通过probobility调整结果
def jieguo(clf,percent,test_data):
    predict = clf.predict(test_data)
    prob = clf.predict_proba(test_data)
    li = [max(i) for i in prob]
    a = zip(predict,li)
    li1 = []
    for k,v in a:
        if v<percent:
            li1.append(0)
        else:
            li1.append(k)
#         li1.append(k+v)
    return li1

# 生成特征函数
def tz(emotion,list_for_cv,list_num_tezheng):

    list_ngram=[]
    list_target=[]
    for filename in file('/home/fish/文档/train/'):
     
        dom = xml.dom.minidom.parse(filename)
        root = dom.documentElement
        for node in dom.getElementsByTagName('sentence'):
            data = re.sub('@[\s\S]*?:','',node.firstChild.data)
            data = re.sub("[^a-zA-Z\u4e00-\u9fa5]","",data)
            if data=='':
                wordList_1=[]
            else:
                wordList_1 = ltp(data) 
            list_ngram.append(n_gram(wordList_1))
            if  node.getAttribute('emotion-1-type')==emotion:
                list_target.append(node.getAttribute('emotion-1-type'))
            else:
                list_target.append('none')
                
    k = 0
    for i in list_target:
        if i =='none':
            list_target[k]=0
            k+=1
        else:
            list_target[k]=1
            k+=1
    print(2)

    e_target = np.array(list_target)
    cv = CountVectorizer()
    cv_model = cv.fit_transform(list_ngram)
    cv_test = cv.transform(list_for_cv)
    train = SelectKBest(chi2,k=15000)
    train_fit = train.fit(cv_model,e_target)
    train_transform = train.transform(cv_test)
    num_tezheng = coo(list_num_tezheng)
    tezheng_new=hstack([train_transform,num_tezheng])

    return tezheng_new

def file(path):
    list_filename = []
    for filename in os.listdir(path=path):
        str_1 = path+filename
        list_filename.append(str_1)
    return list_filename

#检测特殊符号函数
def biaodian(sentense):
    if re.search(r'！！', sentense):
        k = 1
    elif re.search(r'。。', sentense):
        k = 1
    elif re.search(r'？？', sentense):
        k = 1
    elif re.search(r'！？', sentense):
        k = 1
    else:
        k = 0
    return k

#加载情感词典函数
def qgcd(a):
    file = open(a)
    listt = []
    for line in file:
    #去掉换行符
        line=line.strip('\n')
        listt.append(line)
    file.close()
    return listt

#n-gram特征for词袋模型 函数
def n_gram(li):
    list_gram=[]
#     list_gram_1 = []
    for i in range(0,len(li)-1):
        str_gram=''.join(li[i:i+2])
        list_gram.append(str_gram)
    str_gram_1=' '.join(list_gram)
#     list_gram_1.append(str_gram_1)
    return str_gram_1

# 检测否定词 函数
def fdc(str_1):
    list_fdc = qgcd("/home/fish/workspace/my_first_clf/src/dt_clf/dic/foudingci.txt")
    for word in list_fdc:
        match = re.search(word.strip('\n'),str_1)
        if match:
            k = 1
            break
        else:
            k = 0
    return k

# 正则匹配情感词
def zzqgc(k,v):
    
    str_1="'"+'|'.join(k)+"'"
    match = re.search(str_1,v)
    if match:
        a = 1
    else:
        a = 0
    return a

# 情感极性函数
def qgjx(sentense):
    list_1 = []
    for i in range(1,29):
        list_1.append(0)
        
    list_2 = []    
    
    file = open('/home/fish/workspace/my_first_clf/src/dt_clf/dic/qgjx.txt')
    for line in file:
        line=line.strip('\n')
        list_2.append(line)
    file.close()
    
    index = 0
    for l in list_2:
        str_1 = "'"+l+"'"
#         print(str_1)
#         print(str_1)
        reobj = re.compile(str_1)
        if reobj.search(sentense):
            list_1[index]=list_1[index]+1
        index = index+1
        
    return list_1

# 情感强度函数
def qgqd(sentense):
    list_1 = []
    for i in range(1,36):
        list_1.append(0)
#      list1=[0 for i in range(1:36)]   
    list_2 = []    
    
    file = open('/home/fish/workspace/my_first_clf/src/dt_clf/dic/jzqgc.txt')
    for line in file:
        line=line.strip('\n')
        list_2.append(line)
#     list2=[line.strip('\n') for line in file]
    file.close()
    
    index = 0
    for l in list_2:
        str_1 = "r'"+l+"'"
#         print(str_1)
        reobj = re.compile(str_1)
        if reobj.search(sentense):
            list_1[index] = list_1[index]+1
        index = index+1
        
    return list_1

#稀疏矩阵 coo
def coo(list_1):
    row = []
    col = []
    data = []
    a = 0
    for i in list_1:
        b=0
        for k in i:
            if k!=0:
                data.append(k)
                row.append(a)
                col.append(b)
            b=b+1
        a+=1
    data = np.array(data)
    row = np.array(row)
    col = np.array(col)
    c_matrix = coo_matrix((data, (row, col)), shape=(a, len(list_1[0])))
    return c_matrix