class Struct(object):  #以類別方式來模擬結構資料型態
    pass

s=Struct
min_energy_consumption = 0;  #最小消耗能量 
total = 0; #物品重量總和
fb=open("data2.txt","r")
N=int(fb.readline())  #從檔案讀取物品的個數
list1=fb.readline().split() #從檔案讀取物品重量
list2=fb.readline().split() #讀取物品取用次數

obj = []  #物件串列
for i in range(0, len(list1)):  #逐一加入物件資料
    temp=[] #用來暫存各物件的物品重量及取用次數的,預設初值為空串列
    s.w=int(list1[i]) #逐一讀取每一個物品重量
    s.f=int(list2[i]) #逐一讀取每一個物品取用次數
    temp.append(s.w)  #將物品重量加入暫存的串列
    temp.append(s.f)  #將物品取用次數加入暫存的串列
    obj.append(temp)  #以串列為元素的方式附加到物件串列
        
#將最小消耗能量由小到大排序
for i in range(N-1):
    for j in range(N-1-i):
        if obj[j][0]*obj[j+1][1] > (obj[j+1][0]*obj[j][1]):
            obj[j], obj[j+1] = obj[j+1], obj[j]  #互相交換
for i in range(N-1):  #一層一層處理
    total += obj[i][0];  #前面物品重量總和
    min_energy_consumption += total * obj[i+1][1] #最小能量消耗值總和
print("%d" %min_energy_consumption)#輸出最小能量消耗值,以換行結尾
