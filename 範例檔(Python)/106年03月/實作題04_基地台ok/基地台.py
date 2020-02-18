import math
global P  #服務點的距離資訊
global N  #服務點數目
global K  #基地台數目
P=[]

#自訂isCovered函式，測試K個基地台直徑為diameter，
#可否覆蓋所有據點，可以回傳True，不可以回傳False，diameter為基地台直徑。
def isCovered(diameter):
    next_coverage =0
    number = 0
    pos = 0
    while pos<N: #從最前面開始尋找服務點
        next_coverage = P[pos] + diameter;  #基地台的下一個涵蓋範圍
        number=number+1  #記錄基地台數目
        if number>K:
            return False; #如果基地台數量大於K,則傳回False
        if (P[N-1]<=next_coverage) and (number<=K):
            return True;  #如果涵蓋範圍包含全部,則傳回True
        pos=pos+1
        while P[pos]<=next_coverage:
            pos=pos+1

temp=input("請輸入服務點及基地台數,中間以空白隔開,例如:5 2\n").split()
N=int(temp[0])
K=int(temp[1])
temp=input("請輸入各個服務點位置,中間以空白隔開,例如:5 1 2 8 7\n").split()
for i in range(N):
    P.append(int(temp[i]))
P.sort() #由小到大排序
'''
   最小直徑為1，最大直徑為(服務站最大座標-服務站最小座標)/基地台個數+1，
   答案介於這兩數之間，使用二元搜尋找出答案。
'''
min = 1  #最小值從1開始
max = math.floor((P[N-1]-P[0])/K) + 1 #floor是取比參數小之最大整數=ma
while min <= max:
    med = math.floor((min + max) / 2)  #二分搜尋
    if(isCovered(med)):
        max = med
    else:
        min = med + 1
    if min == max:
        break
print("%d" %max)
