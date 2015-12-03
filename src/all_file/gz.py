'''通过对标注文件的人工评价 书写正则匹配规则过滤部分结果'''

import re
  
def re_gz(path,pattern):
    li = [i.strip('\n') for i in open(path)]
    li_w = []
    for i in li:
        if not re.search(pattern, i):
            li_w.append(i)
    f = open(path,'w')
    for i in li_w:
        f.write(i+'\n')
    f.close
    print('done')
     
# nch_wb like     
re_gz('filepath', '什么好奇怪的')
re_gz('filepath', '什么奇怪的')
re_gz('filepath', '我也嫁')
re_gz('filepath', '我也愿意嫁')
re_gz('filepath', '我还不是嫁')
re_gz('filepath', '愿意娶我')
re_gz('filepath', '不就大')
re_gz('filepath', '不就相差')

# nch_wb sadness   
re_gz('filepath', '什么好奇怪的')
re_gz('filepath', '什么奇怪的')
re_gz('filepath', '我也嫁')
re_gz('filepath', '我也愿意嫁')
re_gz('filepath', '我还不是嫁')
re_gz('filepath', '愿意娶我')
re_gz('filepath', '不就大')
re_gz('filepath', '不就相差')

# nch_wb disgust     
re_gz('filepath', '什么好奇怪的')
re_gz('filepath', '什么奇怪的')
re_gz('filepath', '我也嫁')
re_gz('filepath', '我也愿意嫁')
re_gz('filepath', '我还不是嫁')
re_gz('filepath', '愿意娶我')
re_gz('filepath', '不就大')
re_gz('filepath', '不就相差')

# nch_wb surprise
re_gz('filepath', '什么好奇怪的')
re_gz('filepath', '什么奇怪的')
re_gz('filepath', '我也嫁')
re_gz('filepath', '我也愿意嫁')
re_gz('filepath', '我还不是嫁')
re_gz('filepath', '愿意娶我')
re_gz('filepath', '不就大')
re_gz('filepath', '不就相差')
re_gz('filepath', '强子是单身吗')

# nch_wb anger
re_gz('filepath', '什么好奇怪的')
re_gz('filepath', '什么奇怪的')
re_gz('filepath', '我也嫁')
re_gz('filepath', '我也愿意嫁')
re_gz('filepath', '我还不是嫁')
re_gz('filepath', '愿意娶我')
re_gz('filepath', '不就大')
re_gz('filepath', '不就相差')
re_gz('filepath', '要闻回顾')

# nch_wb happiness 
re_gz('filepath', '什么好奇怪的')
re_gz('filepath', '什么奇怪的')
re_gz('filepath', '我也嫁')
re_gz('filepath', '我也愿意嫁')
re_gz('filepath', '我还不是嫁')
re_gz('filepath', '愿意娶我')
re_gz('filepath', '不就大')
re_gz('filepath', '不就相差')

re_gz('filepath', '南都娱乐周刊')

# nch_wb fear
re_gz('filepath', '[害羞]')

# rtt_wb like     
re_gz('filepath', '岩田聪去年因为身体健康状况糟糕而没有参加E3游戏展')

# rtt_wb sadness   
# do not need

# rtt_wb disgust     
# 只抽出一条而且 错了。。。

# rtt_wb surprise
# do not need

# rtt_wb anger
# do not need

# rtt_wb happiness 
re_gz('filepath', '卧槽')
re_gz('filepath', '对索尼来说并不是一个好消息')
re_gz('filepath', '[蜡烛]')

# rtt_wb fear
# do not have

# tj_wb like
     
# 设定参数
# probobility>0.75
# 过滤掉了命名实体

# tj_wb sadness   
re_gz('filepath', '约三里外版本')
re_gz('filepath', '小伍后背缝了40余针')
re_gz('filepath', '不了解')
re_gz('filepath', '黑龙江方正人')
re_gz('filepath', '呵呵')

# tj_wb disgust     
re_gz('filepath', '北京')
re_gz('filepath', '这是在英国每个化工学生都要学习的一场事故')
re_gz('filepath', '有关系')
re_gz('filepath', '我真的不想叫你英雄')

# tj_wb surprise
# do not need

# tj_wb anger
re_gz('filepath', '宝鸡火灾')
re_gz('filepath', '官官相护')
re_gz('filepath', '袁海')


# tj_wb happiness 
# 设定参数
# probobility>0.75
# 过滤掉了命名实体

# tj_wb fear
re_gz('filepath', '约一里版本')
re_gz('filepath', '小编的眼眶湿润了')
re_gz('filepath', '会不会被和谐')

# yyk_wb like     
# 设定参数
# probobility>0.72

# yyk_wb sadness   
re_gz('filepath', '够用吗')
re_gz('filepath', '你能把视频')

# yyk_wb disgust     
re_gz('filepath', '怎么看')
re_gz('filepath', '91porn')
re_gz('filepath', '远看像梨')
re_gz('filepath', '纹身的小伙子')

# yyk_wb surprise
# do not need

# yyk_wb anger
re_gz('filepath', '裸体少年要炸了')
re_gz('filepath', '小编功课没做好')

# yyk_wb happiness 
# 设定参数
# probobility>0.75

# yyk_wb fear
re_gz('filepath', '[害羞]')

