'''通过60000+的句子训练分类器 采用线性核的svc like 和 happiness中使用probobility调整结果使用'''

import xml.dom.minidom
import re
from sklearn import cross_validation
from scipy.sparse import hstack
from collections import Counter
from sklearn import svm
# from sklearn.feature_selection import SelectPercentile,chi2
from sklearn.feature_selection import SelectKBest,chi2
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn import linear_model
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from def_for_clf import qgcd,qgjx,qgqd,coo,biaodian,n_gram,fdc,zzqgc,file,ltp
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.utils import class_weight
# from sklearn.utils import class_weight

#载入情感词典
list_ai = qgcd("/home/fish/workspace/my_first_clf/src/dt_clf/dic+kf+tyc/500w/ai.txt")
list_e = qgcd("/home/fish/workspace/my_first_clf/src/dt_clf/dic+kf+tyc/500w/e.txt")
list_hao = qgcd("/home/fish/workspace/my_first_clf/src/dt_clf/dic+kf+tyc/500w/hao.txt")
list_jing = qgcd("/home/fish/workspace/my_first_clf/src/dt_clf/dic+kf+tyc/500w/jing.txt")
list_ju = qgcd("/home/fish/workspace/my_first_clf/src/dt_clf/dic+kf+tyc/500w/ju.txt")
list_le = qgcd("/home/fish/workspace/my_first_clf/src/dt_clf/dic+kf+tyc/500w/le.txt")
list_nu = qgcd("/home/fish/workspace/my_first_clf/src/dt_clf/dic+kf+tyc/500w/nu.txt")
 
print('ok1')
 

#遍历每个sentence
list_qgqd=[]
list_qgjx=[]
list_ngram=[]
list_for_coo=[]
list_target=[]
 
jishu = 0
 
for filename in file('/home/fish/文档/train/'):
 
    dom = xml.dom.minidom.parse(filename)
    root = dom.documentElement
 
 
# dom = xml.dom.minidom.parse('/home/fish/文档/train/Training data for Emotion Classification.xml')
# root = dom.documentElement
 
# 控制数量
    for node in dom.getElementsByTagName('sentence'):

# 先去掉微博用户名 然后只留下中文和英文字符 其他丢掉        

        data = re.sub('@[\s\S]*?:','',node.firstChild.data)
        data = re.sub("[^a-zA-Z\u4e00-\u9fa5]","",data)
        list_qgqd.append(qgqd(data))
        list_qgjx.append(qgjx(data))
     
     
     
    #     分词
        if data=='':
            wordList=[]
            jishu+=1
        else:
            jishu+=1
            wordList = ltp(data)
        list_ngram.append(n_gram(wordList))
        print(jishu)
        
         
         
    #     否定词特征
        t_fdc = fdc(data)
         
         
     
#     标点特征
        t_bd = biaodian(node.firstChild.data)
    #     情感词典0&1特征
        tmp1 = zzqgc(list_ai,data)
        tmp2 = zzqgc(list_e,data)
        tmp3 = zzqgc(list_hao,data)
        tmp4= zzqgc(list_jing,data)
        tmp5 = zzqgc(list_ju,data)
        tmp6= zzqgc(list_le,data)
        tmp7 = zzqgc(list_nu,data)
     
        numtezheng = [tmp1,tmp2,tmp3,tmp4,tmp5,tmp6,tmp7,len(wordList),t_fdc,t_bd]

 
#     基本特征
 
        list_for_coo.append(numtezheng)
 
# 生成标签    单情感
        if  node.getAttribute('emotion-1-type')=='happiness':
            list_target.append(node.getAttribute('emotion-1-type'))
        else:
            list_target.append('none')
     

    print('do')
print('ok2')
 
# 统计
count1 = Counter(list_target)
print(count1)
 
#特征改0-1
k = 0
for i in list_target:
    if i =='none':
        list_target[k]=0
        k+=1
    else:
        list_target[k]=1
        k+=1
  
 
 
# 统计核对各标签数量
count2 = Counter(list_target)
print(count2)


e_target = np.array(list_target)
 
# 特征生成稀疏矩阵
martix_1 = CountVectorizer().fit_transform(list_ngram)
train_x = SelectKBest(chi2,k=15000).fit_transform(martix_1,e_target)
martix_2 = coo(list_for_coo)

 
# 矩阵合并
coo_1=hstack([train_x,martix_2])
print(coo_1.shape)
 
 
print('ready')

clf = svm.SVC(kernel='linear',class_weight='auto',probability=True)

'''跑分
scores_f1 = cross_validation.cross_val_score(clf, coo_1, e_target, cv=4,scoring='f1_weighted')
print(np.mean(scores_f1))
scores_precision = cross_validation.cross_val_score(clf, coo_1, e_target, cv=4,scoring='precision_weighted')
print(np.mean(scores_precision))
scores_recall = cross_validation.cross_val_score(clf, coo_1, e_target, cv=4,scoring='recall_weighted')
print(np.mean(scores_recall))'''
 
 
 
# for pkl
s = clf.fit(coo_1,e_target)
output = open('/home/fish/桌面/happiness.pkl','wb')
pickle.dump(s, output)
output.close
 

print('done')