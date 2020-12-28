import time

#算差函数
def cha(li):
    for i in range(len(li)):
        if i > 0:
            li[i] = -li[i]
    return sum(li)

#算乘积函数
def chengji(li):
    res = 1
    for i in li:
        res *= i
    return res

#算除函数
def chu(li):
    res = 0
    for i in range(len(li)):
        if i > 0:
            res /= li[i]
        else:
            res = li[i]
    return res

#减少对应的power up函数
def jp(li):
    return str(li).replace('[0,','').replace(']','').replace(' ','-').replace(',',' ')

#卡包增加函数
def pack(num):
    s =''
    j = [0,1,2,3,4,5,6,7,8]
    for w in j:
        for i in range(num):
            s += str(w)+' '
    return s

#时间结束函数
def end(lefttime):
    return time.localtime(time.time() + lefttime)

#激励促销计算函数
def jili(coin_left,feature_cost,p1,p2,p3,p4):
    A = 8/(coin_left/(feature_cost*4))
    li = [pow(max(1,3-p1),2),pow(max(1,3-p2),2),pow(max(1,3-p3),2),pow(max(1,3-p4),2)]
    B = sum(li)/4
    C = abs(A-B)
    return (A,B,C)

if __name__ == '__main__':
    # 算tickets与power up数，可能会有精度问题
    li = [7000,1.2,1.33,1.1,1.3]
    # 算li的和
    print('和：{}'.format(sum(li)))
    # 算li的乘积
    print('积：{}'.format(chengji(li)))
    # 算li的除
    print('除：{}'.format(chu(li)))
    # 算li的差
    print('差：{}'.format(cha(li)))

    #网页上减少对应的power up，一般用于减到0
    pl =[4, 7, 11, 20, 20, 29, 23]

    p = jp(pl)
    print('power up减少列表：{}'.format(p))

    #网页上加卡包数量字符串，示例为每种卡包增加1个
    num = 1
    print('每种卡包增加{}个：'.format(num),pack(num))

    #算促销/活动等结束时间
    lefttime = 0
    t = end(lefttime)
    print('结束时间：{}'.format(t))

    #算激励促销的值,结果分别是A,B,|A-B|
    coin_left = 10
    feature_cost = 1
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    s = jili(coin_left,feature_cost,p1,p2,p3,p4)
    print('A,B,|A-B|：{}'.format(s))

    