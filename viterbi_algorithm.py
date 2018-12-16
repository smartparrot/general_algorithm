import numpy as np
import random


#时间步长
T = 9
h = 5
S = ['p','a','n','d','a']

np.random.seed(0)
data = np.random.rand(h,T)
print('data',data)
# 当前节点的最优父节点的行号，行号是标签序列从上到下排列 0,1 ...,len(h)-1,时间t=0(或j=0)的一列节点没有父节点
BP = [[None for _ in range(T)] for _ in range(h)]
BP = np.array(BP)
# print(BP[1])
# print(BP)
# print(np.array(BP))

# 记录到当前节点(包括当前节点)的最优路径的概率值
score = np.array([[float("-inf") for _ in range(T)] for _ in range(h)])
score[0,0] = data[0,0]
print(score)

# score[1:,0] = float("-inf")
print('score',score) 

print(score)
# print(0 * float("-inf"))
# print(1 if -0.001 > float("-inf") else 0)

for j in range(1,T):
    # print('j',j)
    BP[0,j] = 0
    score[0,j] = score[0,j-1] * data[0,j]
    print('s1',score)
    for i in range(1,min(j+1,h)):#根据CTC的最优估计序列知只能水平向右或右下方
        # print('i',i)
        BP[i,j] = i-1 if score[i-1,j-1] > score[i,j-1] else i
        score[i,j] = data[i,j] * score[BP[i,j],j-1]
    print('b',BP)
    print('s2',score)

print('score',score)
print('BP',BP)

ss = [None for _ in range(T)]
ss[T-1] = h-1

for t in range(T-1,0,-1):
    ss[t-1] = BP[ss[t],t]

print('ss',ss)


# [[None 0 0 0 0 0 0 0 0]
#  [None 0 0 0 0 0 0 0 0]
#  [None None 1 1 1 1 1 1 1]
#  [None None None 2 2 2 2 2 2]
#  [None None None None 3 3 3 3 3]]

# data
# [[0.5488135  0.71518937 0.60276338 0.54488318 0.4236548  0.64589411  0.43758721 0.891773   0.96366276]
#  [0.38344152 0.79172504 0.52889492 0.56804456 0.92559664 0.07103606  0.0871293  0.0202184  0.83261985]
#  [0.77815675 0.87001215 0.97861834 0.79915856 0.46147936 0.78052918  0.11827443 0.63992102 0.14335329]
#  [0.94466892 0.52184832 0.41466194 0.26455561 0.77423369 0.45615033  0.56843395 0.0187898  0.6176355 ]
#  [0.61209572 0.616934   0.94374808 0.6818203  0.3595079  0.43703195  0.6976312  0.06022547 0.66676672]]

# score
#  [[5.48813504e-01 3.92505582e-01 2.36587990e-01 1.28912817e-01  5.46145336e-02 3.52752057e-02 1.54359789e-02 1.37653892e-02 1.32651930e-02]
#  [          -inf 4.34509392e-01 2.29809810e-01 1.34392521e-01  1.24393265e-01 8.83640725e-03 3.07350397e-03 3.12090756e-04  1.14613363e-02]
#  [          -inf           -inf 4.25218861e-01 3.39817295e-01  1.56818668e-01 1.22401546e-01 1.44769726e-02 9.26411908e-03  1.32804193e-03]
#  [          -inf           -inf           -inf 1.12494036e-01  2.63097998e-01 1.20012239e-01 6.95771942e-02 1.30734159e-03  5.72184879e-03]
#  [          -inf           -inf           -inf           -inf  4.04424947e-02 1.14982232e-01 8.37242819e-02 5.04233436e-03  3.36206072e-03]]


# BP [[None 0 0 0 0 0 0 0 0]
#  [None 0 1 0 1 1 0 0 0]
#  [None None 1 2 2 2 2 2 2]
#  [None None None 2 2 3 2 3 2]
#  [None None None None 3 3 3 4 4]]
# ss [0, 1, 2, 2, 3, 3, 4, 4, 4]