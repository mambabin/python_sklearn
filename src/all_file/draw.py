'''通过覆盖率曲线图表示筛选词的覆盖率'''

import re
import numpy as np
import pylab as pl
# 情感对应表情:
# ai:蜡烛
# e:鄙视
# hao:赞
# jing:吃惊
# ju:泪
# le:哈哈
# nu:怒

# 载入词list
li_ci = [i.strip('\n') for i in open('/home/fish/文档/kfjy/惊.txt')]
# 载入匹配句子list
li_sen = [i.strip().split('\t') for i in open('/home/fish/文档/weibo_kf500.txt')]
# 得到句子总数
li_emo = [i[:-1] for i in li_sen if re.sub("[^a-zA-Z\u4e00-\u9fa5]","",str(i[-1:]))=='吃惊']
num_all = len(li_emo)
li_x=[i for i in range(len(li_ci))]
li_y=[]
# 统计词覆盖率
for word in li_ci:
#     计数
    li_emo = [i for i in li_emo if word not in i]
    a = num_all-len(li_emo)
    print(a)

    li_y.append(a/num_all)
    
# print(len(li_x))
# print(len(li_y))
pl.plot(li_x,li_y)
pl.show()