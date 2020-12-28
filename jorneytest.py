def legend_guide_hou(s,k):
    s = s.replace(' ','').replace('[','').replace(']','').strip().split('\n')
    for i in s:
        if '#' in i or 'REWARD' in i:
            print(i)
        li = i.split(',')
        for j in li[k+1:k+2]:
            if j == '':
                continue
            else:
                j = int(j)
                if j < 0:
                    print('钻石*{}'.format(-j))
                elif j == 0:
                    print('duab alter'.format(k))
                elif j < 10:
                    # if j < 5:
                    #     print('{}级卡包'.format(j))
                    # else:
                    #     print('{}星epic卡包'.format(j - 4))
                    if j == 1:
                        print('青铜卡包*1')
                    elif j == 2:
                        print('白银卡包*1')
                    elif j == 3:
                        print('金卡包*1')
                    elif j == 4:
                        print('紫卡包*1')
                    elif j == 5:
                        print('一星卡包*1')
                    elif j == 6:
                        print('二星卡包*1')
                    elif j == 7:
                        print('三星卡包*1')
                    elif j == 8:
                        print('四星卡包*1')
                    elif j == 9:
                        print('五星卡包*1')
                    else:
                        print('未知消息类型'.format(k))
                elif j < 150:
                    p = int(str(j)[:-1])
                    q = int(str(j)[-1])
                    if q == 1:
                        print('single duab*{}'.format(p))
                    elif q == 2:
                        print('xp bottle*{}'.format(p))
                    elif q == 3:
                        print('chest powerup*{}'.format(p))
                    elif q == 4:
                        print('double xp*{}'.format(p))
                    elif q == 5:
                        print('double duab*{}'.format(p))
                    elif q == 6:
                        print('double win*{}'.format(p))
                    elif q == 7:
                        print('instant win*{}'.format(p))
                    elif q == 8:
                        print('uncommon*{}'.format(p))
                    elif q == 9:
                        print('rare*{}'.format(p))
                    else:
                        print('未知消息类型'.format(k))
                elif j >= 150:
                    print('{}'.format(j))
                else:
                    print('未知消息类型'.format(k))

def legend_guide_qian(s):
    s = s.replace(' ','').replace('},','').replace('}','').strip().split('\n')
    for i in s:
        if '<' in i or '-' in i:
            print(i)
        li = i.split('{')
        for j in li[1:]:
            if j == '':
                continue
            else:
                l = j.split(',')
                k = (int)(l[0])
                if len(l) >1:
                    p = (int)(l[1])
                if k == 1:
                    print('duab alter')
                elif k == 2:
                    print('{}'.format(p))
                elif k == 3:
                    print('钻石*{}'.format(p))
                elif k == 4:
                    print('double xp*{}'.format(p))
                elif k == 5:
                    print('double daub*{}'.format(p))
                elif k == 6:
                    print('double win*{}'.format(p))
                elif k == 7:
                    print('instant win*{}'.format(p))
                elif k == 8:
                    print('uncommon*{}'.format(p))
                elif k == 9:
                    print('rare*{}'.format(p))
                elif k == 10:
                    print('金卡包*{}'.format(p))
                elif k == 11:
                    print('紫卡包*{}'.format(p))
                elif k < 17:
                    print('{}星食物袋*{}'.format(k-11,p))
                elif k == 17:
                    print('白银卡包*{}'.format(p))
                elif k == 18:
                    print('{}'.format(p))
                elif k == 19:
                    print('钻石*{}'.format(p))
                elif k == 20:
                    print('一星卡包*{}'.format(p))
                elif k == 21:
                    print('二星卡包*{}'.format(p))
                elif k == 22:
                    print('三星卡包*{}'.format(p))
                elif k == 23:
                    print('四星卡包*{}'.format(p))
                elif k == 24:
                    print('五星卡包*{}'.format(p))
                elif k == 25:
                    print('青铜卡包*{}'.format(p))
                else:
                    print('位置消息类型')
def hzs(s):
    s = s.replace('	','\n')
    print(s)

if __name__ == '__main__':
    #legend guide奖励后端配置
    sgh = '''
GUIDE_REWARD_1 = [
    # < 0 钻石，==0 alert，< 10 卡包，< 150 power，>=150 cash
    [100, 47, 200],
    [200, 0, 24],
    [300, -50, 28],
    [400, 46, 200],
    [500, 400, 2],
    [600, 3, 28],
    [700, 45, -10],
    [800, -50, 200],
    [900, 400, 38],
    [1000, 59, 24],  
    [1100, 46, 200],
    [1200, 400, -10],
    [1300, -50, 28],
    [1400, 47, 200],
    [1500, 400, 2],
    [1600, 3, 28],
    [1700, 45, -15],
    [1800, -80, 200],
    [1900, 400, 38],
    [2000, 59, 24],   
    [2100, 46, 200],
    [2200, 400, -15],
    [2300, -80, 28],
    [2400, 47, 200],
    [2550, 500, 3],
    [2700, 4, 37],
    [2850, 45, -30],
    [3000, -100, 400],
    [3150, 600],
    [3300, 5],
    [3450, 57],
    [3600, 600],
    [3750, -100],
    [3900, 6],
    [4050, 64],
    [4200, 600],
    [4350, -100],
    [4500, 7],
    [4650, 65],
    [4800, -200],  
    [4950, 89],
    [5100, 600],
    [5250, 87]
]
'''
    #k的值0是付费奖励，1是未付费奖励
    k = 1
    # legend_guide_hou(sgh,k)

    # 产品横文案转竖文案
    sj = '''
Double daub*2	钻石*20	double win*2	钻石*20	700	金卡包*1	instant win*2	钻石*20	double xp*2	800	Instant win*3	double win*3	钻石*40	200	Instant win*11	金卡包*1	200	900	钻石*40	Double daub*3	紫卡包*1	1000	钻石*40	Double daub*3	200	一星卡包*1	Instant win*3	钻石*75	1200	Double daub*6	double daub*4	二星卡包	Double xp*4	钻石*75'''
    # hzs(sj)

    sgq = '''
--1，火炬2，现金3，钻石4，双面5，双面6，双面7，瞬时8，不寻常9，稀有，10金袋，11紫袋12-16，食品袋
-- 17, white bag 18, less cash ,19 ,less diamond ,20-24,一星-五星epic卡包,25一级
<--plhd--1/>[1]={
    {7,4},
    {1},
    {3,50},
    {6,4},
    {2,400},
    {10,1},
    {5,4},
    {3,50},
    {2,400},
    {9,5},
    {6,4},
    {2,400},
    {3,50},
    {7,4},
    {2,400},
    {10,1},
    {5,4},
    {3,80},
    {2,400},
    {9,5},
    {6,4},
    {2,400},
    {3,80},
    {7,4},
    {2,500},
    {11,1},
    {5,4},
    {3,100},
    {2,600},
    { 20, 1 },
    {7,5},
    {2,600},
    {3,100},
    { 21, 1 },
    {4,6},
    {2,600},
    {3,100},
    { 22, 1 },
    {5,6},
    {3,200},
    {9,8},
    {2,600},
    {7,8},
}

<--plhd--1/>[1]={
    {18,200},
    {4,2},
    {8,2},
    {18,200},
    {17,1},
    {8,2},
    {19,10},
    {18,200},
    {8,3},
    {4,2},
    {18,200},
    {19,10},
    {8,2},
    {18,200},
    {17,1},
    {8,2},
    {19,15},
    {18,200},
    {8,3},
    {4,2},
    {18,200},
    {19,15},
    {8,2},
    {18,200},
    {10,1},
    {7,3},
    {19,30},
    {18,400}
}
'''
    # legend_guide_qian(sgq)
