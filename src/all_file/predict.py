'''预测新的句子情感'''


from def_for_clf import qgcd,qgjx,qgqd,coo,biaodian,n_gram,ltp_p,fdc,zzqgc,file,tz,ltp, jieguo
import xml.dom.minidom
import jieba
from sklearn.feature_extraction.text import CountVectorizer
import re
from sklearn.feature_selection import SelectKBest,chi2
import pickle
from scipy.sparse import hstack
import numpy as np

#载入情感词典list
list_ai = qgcd("/home/fish/workspace/my_first_clf/src/dt_clf/dic+kf+tyc/500w/ai.txt")
list_e = qgcd("/home/fish/workspace/my_first_clf/src/dt_clf/dic+kf+tyc/500w/e.txt")
list_hao = qgcd("/home/fish/workspace/my_first_clf/src/dt_clf/dic+kf+tyc/500w/hao.txt")
list_jing = qgcd("/home/fish/workspace/my_first_clf/src/dt_clf/dic+kf+tyc/500w/jing.txt")
list_ju = qgcd("/home/fish/workspace/my_first_clf/src/dt_clf/dic+kf+tyc/500w/ju.txt")
list_le = qgcd("/home/fish/workspace/my_first_clf/src/dt_clf/dic+kf+tyc/500w/le.txt")
list_nu = qgcd("/home/fish/workspace/my_first_clf/src/dt_clf/dic+kf+tyc/500w/nu.txt")


list_for_cv=[]
list_num_tezheng=[]
jishu = 0

 
#  载入待预测文件
f = open('/home/fish/文档/标注/file/tj_wb.txt','r')
li1 = [line.strip('\n') for line in f]
f.close()



# 单句测试
# li1 = ['让无数玩家心痛不已岩田聪的离去让。','岩田聪的离去让无数玩家心痛不已。']



# 特征
for i in li1:
    data1 = re.sub('@[\s\S]*?:','',i)
    data1 = re.sub('http://','',data1)
    data_1 = re.sub("[^a-zA-Z\u4e00-\u9fa5]","",data1)
    if data_1=='':
            wordList=[]
            jishu+=1
    else:
            jishu+=1
            wordList_2 = ltp(data_1) 
    list_for_cv.append(n_gram(wordList_2))
    print(jishu)
    t_bd_p = biaodian(i)
    t_fdc_p = fdc(data_1)
    tmp1 = zzqgc(list_ai,data_1)
    tmp2 = zzqgc(list_e,data_1)
    tmp3 = zzqgc(list_hao,data_1)
    tmp4= zzqgc(list_jing,data_1)
    tmp5 = zzqgc(list_ju,data_1)
    tmp6= zzqgc(list_le,data_1)
    tmp7 = zzqgc(list_nu,data_1)
    numtezheng = [tmp1,tmp2,tmp3,tmp4,tmp5,tmp6,tmp7,len(wordList_2),t_fdc_p,t_bd_p]
    list_num_tezheng.append(numtezheng)
    
tezheng_sadness = tz('sadness',list_for_cv,list_num_tezheng)
tezheng_like = tz('like',list_for_cv,list_num_tezheng)
tezheng_disgust = tz('disgust',list_for_cv,list_num_tezheng)
tezheng_surprise = tz('surprise',list_for_cv,list_num_tezheng)
tezheng_anger = tz('anger',list_for_cv,list_num_tezheng)
tezheng_happiness = tz('happiness',list_for_cv,list_num_tezheng)
tezheng_fear = tz('fear',list_for_cv,list_num_tezheng)

# 载入分类器pkl
pickle_like = open('/home/fish/桌面/remove_stmm/like.pkl','rb')
clf_like = pickle.load(pickle_like)
pickle_sadness = open('/home/fish/桌面/remove_stmm/sadness.pkl','rb')
clf_sadness = pickle.load(pickle_sadness)
pickle_disgust = open('/home/fish/桌面/remove_stmm/disgust.pkl','rb')
clf_disgust = pickle.load(pickle_disgust)
pickle_surprise = open('/home/fish/桌面/remove_stmm/surprise.pkl','rb')
clf_surprise = pickle.load(pickle_surprise)
pickle_anger = open('/home/fish/桌面/remove_stmm/anger.pkl','rb')
clf_anger = pickle.load(pickle_anger)
pickle_happiness = open('/home/fish/桌面/remove_stmm/happiness.pkl','rb')
clf_happiness = pickle.load(pickle_happiness)
pickle_fear = open('/home/fish/桌面/remove_stmm/fear.pkl','rb')
clf_fear = pickle.load(pickle_fear)

# predict
print(7)

cp_like = jieguo(clf_like,0.7,tezheng_like)
cp_sadness = clf_sadness.predict(tezheng_sadness)
cp_disgust = clf_disgust.predict(tezheng_disgust)
cp_surprise = clf_surprise.predict(tezheng_surprise)
cp_anger = clf_anger.predict(tezheng_anger)
cp_happiness = jieguo(clf_happiness, 0.75, tezheng_happiness)
cp_fear = clf_fear.predict(tezheng_fear)


# 写入新文件
f_w = open('/home/fish/桌面/test_predict/标注6/remove_stmm/tj_wb0.7_0.75.txt','w')
a = 0
for i in li1:
    if cp_like[a]+cp_sadness[a]+cp_disgust[a]+cp_surprise[a]+cp_anger[a]+cp_happiness[a]+cp_fear[a]==1:
        f_w.write(i+' like:'+str(cp_like[a])+' sadness:'+str(cp_sadness[a])+' disgust:'+str(cp_disgust[a])+' surprise:'+str(cp_surprise[a])+' anger:'+str(cp_anger[a])+' happiness:'+str(cp_happiness[a])+' fear:'+str(cp_fear[a])+'\n')
    a+=1
f_w.close()
print('done')




   
        
# 分割文件        
'''lif = [i.strip('\n') for i in open('/home/fish/文档/标注/wb/predict/yyk_wb_p.txt')]
 
a = '/home/fish/文档/标注/wb/predict/yyk_wb_p/'
for i in lif:
    if re.search('like:1',i):
        f=open(a+'like.txt','a')
        f.write(i+'\n')
        f.close()
    elif re.search('sadness:1',i):
        f=open(a+'sadness.txt','a')
        f.write(i+'\n')
        f.close()
    elif re.search('disgust:1',i):
        f=open(a+'disgust.txt','a')
        f.write(i+'\n')
        f.close()
    elif re.search('surprise:1',i):
        f=open(a+'surprise.txt','a')
        f.write(i+'\n')
        f.close()
    elif re.search('anger:1',i):
        f=open(a+'anger.txt','a')
        f.write(i+'\n')
        f.close()
    elif re.search('happiness:1',i):
        f=open(a+'happiness.txt','a')
        f.write(i+'\n')
        f.close()
    elif re.search('fear:1',i):
        f=open(a+'fear.txt','a')
        f.write(i+'\n')
        f.close()
    else:
        f=open(a+'none.txt','a')
        f.write(i+'\n')
        f.close()
    print('going')   
print('done')'''