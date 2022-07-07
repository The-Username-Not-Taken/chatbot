import random
import jieba
import pandas as pd
import logging

jieba.setLogLevel(logging.INFO)

nameList = ['甜菊汽水','晚晚星河','海与迟落','素年凉音','眉眼动人','车窗起雾','无意争春','此去经年','一纸情书','期限浪漫','倦鸟归林','就像当初','梦在深巷','眼底星碎','伴君终老','日落于西','无情有思','无人倾听','不见不念','人间无味','青杉依旧','念卿天涯','暂停白昼','星落山间','始于初见','摘碗月亮','心动不足','落日海湾','黎夕旧梦','北島春渡','遍野温柔','孤烟往事','了断爱情','折扇轻晃','江南未寒','海棠未眠','一念痴狂','哭蓝了海','爱上孤独','像梦一场','不畏山海','转念成空','曲终人散','细雨流光','万鲸成海','夏日浅笑','温柔的风','落荒而逃','随梦而飞','月牙弯弯','钱比心真','情归何处','半盏清酒','跨越山海','可盐可甜','不曾遇见','清远楼阁','君非梓沐','一尾流莺','月球罚站','陌上烟雨','夜雨寄北','仅存姿态','逆流的泪','伈随风飞','首选心动','林深见鹿','冷心为帝','繁华落尽','江山错落','半糖芝士','一切随意','归落银河','遥远的她','一身仙气','清欢百味','一生所爱','凌晨入眠','半夏无爱','陌路独白','无言温柔']
aiName = nameList[random.randint(0,80)]
print(aiName + ':\n欢迎来到AI智能聊天机器人，这里是' + aiName + '，我们可以开始对话了，请输入...\n')

emoWords = pd.read_csv('C:\Old Folder\玩\smart_chatbot\情感词汇.csv', sep = ', ', engine = 'python', index_col = '词语') # AI 暗地里拿了一本词典学习人类语言的情感

wordlist = ['典', '典中典', '乐', '笑嘻了', '绷', '蚌'] # 对线三大件：典乐蚌

fuduji = ''

while True:
    print('您:')
    inp = input('')
    if inp == 'exit()':
        exit()
    if fuduji != '' and ((fuduji in inp) or (inp in fuduji)):
        output = '复读机是吧😅'
    else:
        output = ''
        inpCut = jieba.lcut(inp)
        rep = ''
        jileConstant = 0 

        for i in (0,len(inpCut) - 1):
            if len(inpCut) > 1:
                if inpCut[i] == rep:
                    output = '急了急了'
                    break
            rep = inpCut[i] # 检测有没有重复用词，如果重复表示用户急了
            jileConstant_temp = 0

            try:
                if emoWords.loc[inpCut[i]]['情感分类'] in ['NA', 'NI', 'NC', 'NG', 'NE', 'ND', 'NN', 'NK', 'NL']:
                    jileConstant_temp = emoWords.loc[inpCut[i]]['强度']
            except:
                continue # 在大连理工词表里检测这个词急不急，并查找这个词的强度，找不到算了

            jileConstant = jileConstant + jileConstant_temp

        if len(inpCut) >= 5:
            if jileConstant >= 5:
                output = '急了😅'
            if jileConstant >= 10:
                output = '急了急了'
            if jileConstant >= 20:
                output = '急了急了😅'
        elif len(inpCut) <= 5 and jileConstant > 0:
            output = '急了'
            # 采用大连理工词表，如果用户发言里有情感为愤怒或者惊恐的词汇，则表示用户急了；强度越高，则AI会说更多的急了以及增加流汗黄豆，方便更好地治疗低血压
        
        if output == '':
            ran = random.randint(0,6) # 随机生成典乐蚌三大件
            if ran == 6 or (aiName in inp):
                output = '😅' # 如果用户重复了AI用户名，则AI冷眼相待，十分高冷
            else:
                output = wordlist[ran]
                emo = random.randint(1,10)
                if emo > 7:
                    output = output + '😅' # 随机添加流汗黄豆
    print('\n' + aiName + ':\n' + output + '\n')
    fuduji = output

# References:
# 大连理工大学中文情感词汇本体库
