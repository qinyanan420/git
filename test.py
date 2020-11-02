'''
备注：配置必须顶格写
'''

#产品横文案转竖文案
def hzs(s):
    s = s.replace('	','\n')
    print(s)

#前端与文字转化准备
def transform(s):
    li = s.strip().split('\n')
    lis = [[] for i in range(len(li))]
    num = 0
    for i in li:
        if '+' in i:
            j = i.split('+')
            for k in j:
                m = k.split('*')
                typecode(lis,num,m)
        else:
            j = i.split('\n')
            for k in j:
                t = k.split('{')[1:]
                typestr(lis,num,t)
        num += 1
    return lis

#文字转前端代码的逻辑
def typecode(lis,num,m):
    if 'missing' in m[0]:
        lis[num].append(['4', '2', '0', '1'])
    elif 'wild' in m[0]:
        lis[num].append(['4', '1', '0', '1'])
    else:
        if '选卡' in m[0]:
            p = '1'
        else:
            p = '0'
        if '铜' in m[0]:
            lis[num].append(['1','1',p,m[1]])
        elif '银' in m[0]:
            lis[num].append(['1','2',p,m[1]])
        elif '金' in m[0]:
            lis[num].append(['1','3',p,m[1]])
        elif '钻石' in m[0]:
            lis[num].append(['1','4',p,m[1]])
        else:
            x = m[0].split('星')
            n = int(x[0])
            if 'treasure' in m[0]:
                lis[num].append(['3',str(n),'0',m[1]])
            elif '宝箱' in m[0]:
                lis[num].append(['1',str(n+4),p,m[1]])
            else:
                lis[num].append(['2',str(n),'0',m[1]])

#前端转中文情况（前端公告版）
def typestr(lis,num,t):
    for o in t:
        p = o[0]
        q = o[2]
        r = o[4]
        s = o[6]
        if p == '4':
            if q == '1':
                lis[num].append('Wild*1')
            else:
                lis[num].append('Missing*1')
        elif p == '3':
            lis[num].append(str(q) + '星treasure卡*' + str(s))
        elif p == '2':
            lis[num].append(str(q) + '星legend' + '卡*' + str(s))
        else:
            if r == '0':
                f = ''
            else:
                f = '选卡'
            if q == '1':
                lis[num].append('铜'+f+'*'+str(s))
            elif q == '2':
                lis[num].append('银'+f+'*'+str(s))
            elif q == '3':
                lis[num].append('金'+f+'*'+str(s))
            elif q == '4':
                lis[num].append('钻石'+f+'*'+str(s))
            else:
                lis[num].append(str(int(q)-4) + '星legend' + f + '宝箱*' + str(s))

#前端typestr/typecode列表按照中文格式输出
def printing(lis):
    for i in lis:
        i.reverse()
    for i in lis:
        if '*' in i[0]:
            print(str(i).replace('\'', '').replace(',', '+').replace(' ','')[1:-1])
        else:
            print(str(i).replace('[', '{').replace(']', '}').replace('\'', '').replace(' ','')[1:-1])

#后端代码转文字的逻辑（PASS/TRAIL/活动）
def hou(sh):
    j = str(sh).replace('[','').replace(']','').\
        replace(',','').replace('(','').replace(')','').strip('\n').strip()
    t = j.strip().split('\n')
    for x in t:
        t[0] = '#'+x
        print(x)
        break
    for x in t:
        if x == '    'or '':
            continue
        if '#' in x:
            continue
        else:
            y = x.strip().split(' ')
            if y != ' ':
                for i in range(len(y)):
                    if y[i] != '':
                        z = y[i:]
                        break
        if len(z) == 3:
            if 'BRONZE' in z[0]:
                print('铜选卡*'+z[1])
            elif 'SILVER' in z[0]:
                print('银选卡*'+z[1])
            elif 'SUPERGOLD' or 'DIAMOND' in z[0]:
                print('钻石选卡*' + z[1])
            elif 'GOLD' in z[0]:
                print('金选卡*'+z[1])
            elif 'LEGEND_CHEST3' in z[0]:
                print('3星传奇选卡宝箱*'+z[1])
            elif 'LEGEND_CHEST4' in z[0]:
                print('4星传奇选卡宝箱*'+z[1])
            elif 'LEGEND_CHEST5' in z[0]:
                print('5星传奇选卡宝箱*'+z[1])
            else:
                print('缺少数据类型')
        elif len(z) == 2 or len(z) == 4:
            if 'BRONZE' in z[0]:
                print('铜*'+z[1])
            elif 'SILVER' in z[0]:
                print('银*'+z[1])
            elif 'SUPERGOLD' in z[0]:
                print('钻石*' + z[1])
            elif 'GOLD' in z[0]:
                print('金*'+z[1])
            elif 'LEGEND_CHEST3' in z[0]:
                print('3星传奇宝箱*'+z[1])
            elif 'LEGEND_CHEST4' in z[0]:
                print('4星传奇宝箱*'+z[1])
            elif 'LEGEND_CHEST5' in z[0]:
                print('5星传奇宝箱*'+z[1])
            elif 'TICKETS' in z[0]:
                print('TICKETS*' + z[1])
            elif 'DOUBLE_XP' in z[0]:
                print('DOUBLE_XP*' + z[1])
            elif 'DOUBLE_DAUB' in z[0]:
                print('DOUBLE_DAUB*' + z[1])
            elif 'DOUBLE_PAYOUT' in z[0]:
                print('DOUBLE_PAYOUT*' + z[1])
            elif 'INSTANT_WIN' in z[0]:
                print('INSTANT_WIN*' + z[1])
            elif 'RARE' in z[0]:
                print('RARE*' + z[1])
            elif 'UNCOMMON' in z[0]:
                print('UNCOMMON*' + z[1])
            elif 'DIAMOND' in z[0]:
                print('钻石*' + z[1])
            elif 'LEGEND3_CARD' in z[0]:
                print('3星传奇卡*' + z[1])
            elif 'LEGEND4_CARD' in z[0]:
                print('4星传奇卡*' + z[1])
            elif 'LEGEND5_CARD' in z[0]:
                print('5星传奇卡*'+z[1])
            elif 'ALERT' in z[0]:
                print('ALERT*' + z[1])
            elif 'MISSING_CARD' in z[0]:
                print('MISSING_CARD*' + z[1])
            elif 'WILD_CARD' in z[0]:
                print('WILD_CARD*' + z[1])
            elif 'TREASURE_CARD5' in z[0]:
                print('5星treasure*' + z[1])
            elif 'TREASURE_CARD4' in z[0]:
                print('4星treasure*' + z[1])
            elif 'TREASURE_CARD3' in z[0]:
                print('3星treasure*' + z[1])
            elif 'TREASURE5_CARD' in z[0]:
                print('5星treasure*' + z[1])
            elif 'TREASURE4_CARD' in z[0]:
                print('4星treasure*' + z[1])
            elif 'TREASURE3_CARD' in z[0]:
                print('3星treasure*' + z[1])
            else:
                print('缺少数据类型')
        else:
            continue

#前段奖励根据活动进行分类（cook/trip/garden）
def typesr(sr):
    lis = sr.strip().split('},')
    for o in lis:
        o = o.replace('{','').replace('}','').replace('\n','').strip()
        if o is '':
            continue
        # cook活动
        # p = o[0]
        # q = o[2]
        # r = o[4]
        # s = o[6]
        # if p == '2':
        #     if q == '1':
        #         print('Missingcard*1')
        #     elif q == '2':
        #         print('4星Treasure*1')
        #     elif q == '3':
        #         print('Wild*1')
        #     else:
        #         print('未知消息类型')
        # else:
        #     if r == '0':
        #         f = ''
        #     else:
        #         f = '选卡'
        #     if q == '1':
        #         print('铜' + f + '*' + str(s))
        #     elif q == '2':
        #         print('银' + f + '*' + str(s))
        #     elif q == '3':
        #         print('金' + f + '*' + str(s))
        #     elif q == '4':
        #         print('钻石' + f + '*' + str(s))
        #     else:
        #         print(str(int(q) - 2) + '星legend' + f + '宝箱*' + str(s))

        # trip活动
        #trip活动宝箱奖励
        # p = o[0]
        # q = o[2]
        # r = o[4]
        # if r == '1':
        #     f = ''
        # else:
        #     f = '选卡'
        # if q == '1':
        #     print('铜' + f + '*' + str(p))
        # elif q == '2':
        #     print('银' + f + '*' + str(p))
        # elif q == '3':
        #     print('金' + f + '*' + str(p))
        # elif q == '4':
        #     print('钻石' + f + '*' + str(p))
        # else:
        #     print(str(int(q) - 4) + '星legend' + f + '宝箱*' + str(p))
        #trip活动额外奖励
        # p = o[0]
        # q = o[2]
        # r = o[4]
        # if p == '0':
        #     continue
        # else:
        #     if r == '3':
        #         print(str(q)+'星treasure*1')
        #     elif r == '4':
        #         print(str(q)+'星legend*1')
        #     elif r == '5':
        #         print('Wild*1')
        #     elif r == '6':
        #         print('Missing*1')
        #     else:
        #         print('未知消息类型')

        #garden活动
        #garden活动宝箱奖励
        # p = o[0]
        # q = o[2]
        # r = o[4]
        # if q == '4':
        #     print(str(r)+ '星legend*' + str(p))
        # elif q == '3':
        #     print('Wild*1')
        # elif q == '2':
        #     print(str(r)+ '星Treasure*' + str(p))
        # else:
        #     if r == '1':
        #         print('铜' + '*' + str(p))
        #     elif r == '2':
        #         print('银' + '*' + str(p))
        #     elif r == '3':
        #         print('金' + '*' + str(p))
        #     elif r == '4':
        #         print('钻石' + '*' + str(p))
        #     else:
        #         print(str(int(q) - 4) + '星legend宝箱*' + str(p))
        #garden活动额外奖励
        # p = o[0]
        # q = o[2]
        # r = o[4]
        # if q == '4':
        #     print(str(r)+ '星legend*' + str(p))
        # elif q == '3':
        #     if r == '1':
        #         print('Wild*1')
        #     elif r == '2':
        #         print('Missingcard*1')
        #     else:
        #         print('未知消息类型')
        # elif q == '2':
        #     print(str(r)+ '星Treasure*' + str(p))
        # else:
        #     if r == '1':
        #         print('铜' + '*' + str(p))
        #     elif r == '2':
        #         print('银' + '*' + str(p))
        #     elif r == '3':
        #         print('金' + '*' + str(p))
        #     elif r == '4':
        #         print('钻石' + '*' + str(p))
        #     else:
        #         print(str(int(q) - 4) + '星legend宝箱*' + str(p))

        # flash活动
        p = o[0]
        q = o[2]
        r = o[4]
        s = o[6]
        if p == '2':
            if q == '1':
                print('wildcard*1')
            elif q == '2':
                print('Missingcard*1')
        else:
            if r == '0':
                f = ''
            else:
                f = '选卡'
            if q == '1':
                print('铜' + f + '*' + str(s))
            elif q == '2':
                print('银' + f + '*' + str(s))
            elif q == '3':
                print('金' + f + '*' + str(s))
            elif q == '4':
                print('钻石' + f + '*' + str(s))
            else:
                print(str(int(q) - 4) + '星legend' + f + '宝箱*' + str(s))
if __name__ == "__main__":
#产品横文案转竖文案
    sj = '''
铜	铜	银	金	3星Treasure卡	3星legend卡	3星legend宝箱+Missing	3星legend宝箱
铜	铜	银	金	3星Treasure卡	3星legend卡	3星legend宝箱+Missing	3星legend宝箱
铜	银	银	金	3星Treasure卡	3星legend卡	3星legend宝箱+Missing	3星legend宝箱
银	银	银	金	3星Treasure卡	3星legend卡	3星legend宝箱+Missing	3星legend宝箱
银	银	金	金	3星Treasure卡	3星legend卡	4星legend宝箱+Missing	4星legend宝箱
银	金	金	钻石	3星Treasure卡	3星legend卡	4星legend宝箱+Missing	4星legend宝箱
银	金	金	钻石	3星Treasure卡	3星legend卡	4星legend宝箱+Missing	4星legend宝箱
金	金	金	钻石	3星Treasure卡	3星legend卡	4星legend宝箱+Missing	4星legend宝箱
金	金	钻石	钻石	3星Treasure卡	3星legend卡	4星legend宝箱+Missing	4星legend宝箱
金	金	钻石	钻石	3星Treasure卡	3星legend卡	4星legend宝箱+Missing	4星legend宝箱
'''

#前端公告板转中文
    sc = '''
{4,2,0,1},{1,7,0,1},{2,3,0,1},{3,3,0,1},{1,3,0,1},{1,2,0,1},{1,1,0,2}
{4,2,0,1},{1,7,0,1},{2,3,0,1},{3,3,0,1},{1,3,0,1},{1,2,0,1},{1,1,0,2}
{4,2,0,1},{1,7,0,1},{2,3,0,1},{3,3,0,1},{1,3,0,1},{1,2,0,2},{1,1,0,1}
{4,2,0,1},{1,7,0,1},{2,3,0,1},{3,3,0,1},{1,3,0,1},{1,2,0,3}
{4,2,0,1},{1,8,0,1},{2,3,0,1},{3,3,0,1},{1,3,0,2},{1,2,0,2}
{4,2,0,1},{1,8,0,1},{2,3,0,1},{3,3,0,1},{1,4,0,1},{1,3,0,2},{1,2,0,1}
{4,2,0,1},{1,8,0,1},{2,3,0,1},{3,3,0,1},{1,4,0,1},{1,3,0,2},{1,2,0,1}
{4,2,0,1},{1,8,0,1},{2,3,0,1},{3,3,0,1},{1,4,0,1},{1,3,0,3}
{4,2,0,1},{1,8,0,1},{2,3,0,1},{3,3,0,1},{1,4,0,2},{1,3,0,2}
{4,2,0,1},{1,8,0,1},{2,3,0,1},{3,3,0,1},{1,4,0,2},{1,3,0,2}
'''

#前端奖励转中文
    sr = '''
{
        {{{1,1,0,1}}, {{1,1,0,2}}, {{1,2,0,1}}, {{1,3,0,1}}, {{1,7,0,1},{2,2,0,1}}}, --1 wild 2 missing
        {{{1,1,0,1}}, {{1,1,0,2}}, {{1,2,0,1}}, {{1,3,0,1}}, {{1,7,0,1},{2,2,0,1}}},
        {{{1,1,0,2}}, {{1,2,0,1}}, {{1,2,0,2}}, {{1,3,0,1}}, {{1,7,0,1},{2,2,0,1}}},
        {{{1,1,0,2}}, {{1,2,0,1}}, {{1,2,0,2}}, {{1,3,0,1}}, {{1,7,0,1},{2,2,0,1}}},
        {{{1,1,0,2}}, {{1,2,0,1}}, {{1,3,0,1}}, {{1,3,0,2}}, {{1,8,0,1},{2,2,0,1}}},
        {{{1,1,0,2}}, {{1,2,0,2}}, {{1,3,0,1}}, {{1,3,0,2}}, {{1,8,0,1},{2,2,0,1}}},
        {{{1,2,0,1}}, {{1,2,0,2}}, {{1,3,0,2}}, {{1,4,0,1}}, {{1,8,0,1},{2,2,0,1}}},
        {{{1,2,0,1}}, {{1,3,0,1}}, {{1,3,0,2}}, {{1,4,0,1}}, {{1,8,0,1},{2,2,0,1}}},
        {{{1,2,0,2}}, {{1,3,0,2}}, {{1,4,0,1}}, {{1,4,1,1}}, {{1,8,0,1},{2,2,0,1}}},
        {{{1,2,0,2}}, {{1,3,0,2}}, {{1,4,0,1}}, {{1,4,1,1}}, {{1,8,0,1},{2,2,0,1}}},
    },
    {
        {{{1,1,0,1}}, {{1,1,0,2}}, {{1,2,0,1}}, {{1,3,0,1}}, {{1,7,0,1}}},
        {{{1,1,0,1}}, {{1,1,0,2}}, {{1,2,0,1}}, {{1,3,0,1}}, {{1,7,0,1}}},
        {{{1,1,0,2}}, {{1,2,0,1}}, {{1,2,0,2}}, {{1,3,0,1}}, {{1,7,0,1}}},
        {{{1,1,0,2}}, {{1,2,0,1}}, {{1,2,0,2}}, {{1,3,0,1}}, {{1,7,0,1}}},
        {{{1,1,0,2}}, {{1,2,0,1}}, {{1,3,0,1}}, {{1,3,0,2}}, {{1,8,0,1}}},
        {{{1,1,0,2}}, {{1,2,0,2}}, {{1,3,0,1}}, {{1,3,0,2}}, {{1,8,0,1}}},
        {{{1,2,0,1}}, {{1,2,0,2}}, {{1,3,0,2}}, {{1,4,0,1}}, {{1,8,0,1}}},
        {{{1,2,0,1}}, {{1,3,0,1}}, {{1,3,0,2}}, {{1,4,0,1}}, {{1,8,0,1}}},
        {{{1,2,0,2}}, {{1,3,0,2}}, {{1,4,0,1}}, {{1,4,1,1}}, {{1,8,0,1}}},
        {{{1,2,0,2}}, {{1,3,0,2}}, {{1,4,0,1}}, {{1,4,1,1}}, {{1,8,0,1}}},
    }
'''

#后端代码转化文字
    sh ='''
GARDEN_REWARD_CARD = [
    # group_0
    [
     [GARDEN_REWARD_BRONZE_CHEST, 1],
     [GARDEN_REWARD_BRONZE_CHEST, 1],
     [GARDEN_REWARD_SILVER_CHEST, 1],
     [GARDEN_REWARD_GOLD_CHEST, 1],
     [GARDEN_REWARD_TREASURE3_CARD, 1],
     [GARDEN_REWARD_LEGEND3_CARD, 1]
     ],
    # group_1
    [
     [GARDEN_REWARD_BRONZE_CHEST, 1], 
     [GARDEN_REWARD_BRONZE_CHEST, 1],
     [GARDEN_REWARD_SILVER_CHEST, 1],
     [GARDEN_REWARD_GOLD_CHEST, 1],
     [GARDEN_REWARD_TREASURE3_CARD, 1], 
     [GARDEN_REWARD_LEGEND3_CARD, 1]],
    # group_2
    [
     [GARDEN_REWARD_BRONZE_CHEST, 1],
     [GARDEN_REWARD_SILVER_CHEST, 1],
     [GARDEN_REWARD_SILVER_CHEST, 1],
     [GARDEN_REWARD_GOLD_CHEST, 1],
     [GARDEN_REWARD_TREASURE3_CARD, 1],
     [GARDEN_REWARD_LEGEND3_CARD, 1]],
    # group_3
    [
     [GARDEN_REWARD_SILVER_CHEST, 1],
     [GARDEN_REWARD_SILVER_CHEST, 1],
     [GARDEN_REWARD_SILVER_CHEST, 1],
     [GARDEN_REWARD_GOLD_CHEST, 1],
     [GARDEN_REWARD_TREASURE3_CARD, 1],
     [GARDEN_REWARD_LEGEND3_CARD, 1]],
    # group_4
    [
     [GARDEN_REWARD_SILVER_CHEST, 1], 
     [GARDEN_REWARD_SILVER_CHEST, 1],
     [GARDEN_REWARD_GOLD_CHEST, 1],
     [GARDEN_REWARD_GOLD_CHEST, 1],
     [GARDEN_REWARD_TREASURE3_CARD, 1], 
     [GARDEN_REWARD_LEGEND3_CARD, 1]],
    # group_5
    [
     [GARDEN_REWARD_SILVER_CHEST, 1], 
     [GARDEN_REWARD_GOLD_CHEST, 1],
     [GARDEN_REWARD_GOLD_CHEST, 1], 
     [GARDEN_REWARD_SUPERGOLD_CHEST, 1],
     [GARDEN_REWARD_TREASURE3_CARD, 1], 
     [GARDEN_REWARD_LEGEND3_CARD, 1]],
    # group_6
    [
     [GARDEN_REWARD_SILVER_CHEST, 1], 
     [GARDEN_REWARD_GOLD_CHEST, 1],
     [GARDEN_REWARD_GOLD_CHEST, 1], 
     [GARDEN_REWARD_SUPERGOLD_CHEST, 1],
     [GARDEN_REWARD_TREASURE3_CARD, 1], 
     [GARDEN_REWARD_LEGEND3_CARD, 1]],
    # group_7
    [
     [GARDEN_REWARD_GOLD_CHEST, 1], 
     [GARDEN_REWARD_GOLD_CHEST, 1],
     [GARDEN_REWARD_GOLD_CHEST, 1], 
     [GARDEN_REWARD_SUPERGOLD_CHEST, 1],
     [GARDEN_REWARD_TREASURE3_CARD, 1], 
     [GARDEN_REWARD_LEGEND3_CARD, 1]],
    # group_8
    [
     [GARDEN_REWARD_GOLD_CHEST, 1], 
     [GARDEN_REWARD_GOLD_CHEST, 1],
     [GARDEN_REWARD_SUPERGOLD_CHEST, 1], 
     [GARDEN_REWARD_SUPERGOLD_CHEST, 1],
     [GARDEN_REWARD_TREASURE3_CARD, 1], 
     [GARDEN_REWARD_LEGEND3_CARD, 1]],
    # group_9
    [
     [GARDEN_REWARD_GOLD_CHEST, 1], 
     [GARDEN_REWARD_GOLD_CHEST, 1],
     [GARDEN_REWARD_SUPERGOLD_CHEST, 1], 
     [GARDEN_REWARD_SUPERGOLD_CHEST, 1],
     [GARDEN_REWARD_TREASURE3_CARD, 1], 
     [GARDEN_REWARD_LEGEND3_CARD, 1]],
]
'''

# hzs(sj)
# hou(sh)
# lis = transform(sc)
# printing(lis)
typesr(sr)
