global root   #根節點的編號
global sum_of_highest #所有節點的高度總和
global maxumun #目前最大高度
sum_of_highest=0
maxumun=0
root=0

def h(data,no):  #計算節點的高度
    height=0  #記錄目前最大的高度,預設值為0
    if data[no-1][1]==0: return 0 #葉節點為遞迴函數的結束出口
    else:
        for i in range(2,data[no-1][1]+2):
            temp=h(data,data[no-1][i])+1
            height = max(temp,height)
        return height; #傳回子節點最大的高度

fb=open("data2.txt","r")
n=int(fb.readline())  #n記錄節點總數
data=[]*100
for i in range(n): #輸入每列資料
    subnode=fb.readline().split()
    num_of_childnode=int(subnode[0]) #暫存每列子節點數
    row=[]
    row.append(i+1) #第一個元素為列編號
    row.append(num_of_childnode)  #每列子節點數
    if num_of_childnode>0: #有子節點才輸入
        for j in range(2,num_of_childnode+2):
            row.append(int(subnode[j-1]))
    data.append(row)
for i in range(1,n+1): #依序計算每一節點的最大高度
    hi=h(data,i)   #節點的最大高度
    if hi>maxumun:     #如果該節點高度大於目前最大高度
        maxumun=hi;      #將 hi 設為目前最大高度
        root=i;         #將該節點編號設為根節點編號
    sum_of_highest+=hi; #累計所有節點的最大高度

print("%d" %root);   #根節點編號
print("%d" %sum_of_highest); #所有節點最大高度總和
