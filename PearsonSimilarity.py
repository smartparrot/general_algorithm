import numpy as np

# x为数字列表
def calnonzero(x):
    i = 0
    for xi in x:
        if xi != 0:
            i = i + 1
    print(i)
    return i

def pearsonsimilarity(a,b):
    # ua = np.sum(a)/calnonzero(a)
    # ub = np.sum(b)/calnonzero(b)
    ua = np.mean(a)
    ub = np.mean(b)
    au = a -ua
    bu = b -ub
    print('au',au,'bu',bu)
    denominator = (np.sum(np.square(au)))**0.5 * (np.sum(np.square(bu)))**0.5
    return np.dot(au,bu)/denominator


# pearsonsimilarity1运算结果与讲义中的一样
def pearsonsimilarity1(a,b):
    ua = np.sum(a)/calnonzero(a)
    ub = np.sum(b)/calnonzero(b)
    au = [ai-ua if ai !=0 else 0 for ai in a]
    bu = [bi-ub if bi !=0 else 0 for bi in b]
    print('au',au,'bu',bu)
    denominator = (np.sum(np.square(au)))**0.5 * (np.sum(np.square(bu)))**0.5
    return np.dot(au,bu)/denominator

# a需要为用户估计评分的那个物品向量
a = [1,0,3,0,0,5,0,0,5,0,4,0]
b = [0,0,5,4,0,0,4,0,0,2,1,3]
c = [1,0,3,0,3,0,0,2,0,0,4,0]

num = pearsonsimilarity1(a,b)
print(num)

num = pearsonsimilarity1(a,a)
print(num)

num = pearsonsimilarity1(a,c)
print(num)

# num = pearsonsimilarity(a,b)
# print(num)

# num = pearsonsimilarity(a,a)
# print(num)

