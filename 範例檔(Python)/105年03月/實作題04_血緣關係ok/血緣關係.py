#函式distance計算中間過程最大深度 
def distance(x):
    global CHILD, farthest_blood_distance
    #最大前兩個的深度
    farthest1 = 0  #向下的最大值
    farthest2 = 0  #向下的第二大值
    depth = 0  #記錄家族成員的深度
    if len(CHILD[x]) == 0:  return 0  #沒有小孩是遞迴的出口條件
    if len(CHILD[x]) == 1:  return distance(CHILD[x][0]) + 1#只有一個小孩
    else:  #2個小孩以上
        '''
        走訪每一個小孩，找出最大深度的前兩名，
        最大深度儲存到farthest1，
        第二大深度儲存到farthest2
        '''
        for i in range(0, len(CHILD[x])):  #逐一處理每一個小孩
            depth = distance(CHILD[x][i]) + 1
            if i == 0:  farthest1 = depth  #第1個小孩即為最大值
            elif i == 1:  #走訪第二個小孩時
                #如果最大深度大於原先的depth,則將它設定為第二大深度
                if depth <= farthest1:  farthest2 = depth  
                else:
                    '''
		    如果最大深度小於 depth，
		    則將 depth設定成最大深度farthest1， 
		    原先的最大深度farthest1，設定為第二大深度farthest2
		    '''
                    farthest2 = farthest1
                    farthest1 = depth
            else:  #走訪第三個小孩以後 
                if depth >= farthest1:  
                    '''
		    如果depth大於或等於最大深度 farthest1，
		    原先的farthest1設定給第二大深度farthest2
		    再將depth設定給最大深度 farthest1
		    ''' 
                    farthest2 = farthest1
                    farthest1 = depth
                elif depth > farthest2:
                    '''
		    若大於第二大深度farthest2， 
		    則將 depth設定給第二大深度farthest2
		    '''
                    farthest2 = depth  
        '''
	中間的節點的分支度大於等於2，
	最大血緣距離為小孩中farthest1與第farthest2相加， 
	再和原先的 farthest_blood_distance取較大值 
	'''
        farthest_blood_distance = max(farthest_blood_distance,
                                      farthest1+farthest2)
        '''
	由上到下找尋過程，當分支度只有1時，
	回傳該家族成員的最大深度 farthest1
        '''
        return farthest1  #傳回該人員編號向下單向搜尋的最大值

fp=open("data2.txt","r")  #開啟測試資料檔
n=int(fp.readline()) 
from_root = 0  #distance傳回值,單一節點向下找的最大值
farthest_blood_distance = 0  #即本題要求的最遠血緣距離
isChild = []  #記錄這位家庭成員是否為其他人的小孩
CHILD = []  #記錄家族關係樹狀圖,CHILD的元素為串列
for i in range(0, n):  
    isChild.append(False)
    CHILD.append([])  #CHILD的元素為串列
for i in range(1, n):
    tem=fp.readline().split(' ')
    node1 = int(tem[0])
    node2 = int(tem[1])
    CHILD[node1].append(node2)  #node2為node1的小孩
    isChild[node2] = True  #此處node2是小孩，設定isChild為true
for i in range(0, n):  #找出最上層人沒有父節點的人員編號root
    if isChild[i] == False:
        root = i
        break
from_root = distance(root)  #由root開始向下尋找
'''
from_root為從root出發最大深度
farthest_blood_distance為中間過程最大深度，
兩者間取取最大值 
'''
farthest_blood_distance = max(from_root, farthest_blood_distance) 
print(farthest_blood_distance)
