class Struct(object):
    pass
s = Struct()
place=[]
in1 = input('請輸入n m k三變數的值,中間以空白隔開: ')
temp=in1.split()
n=int(temp[0])
m=int(temp[1])
k=int(temp[2])
#建立環狀鏈結串列
for i in range(n-1):
    temp=[]
    s.data=i+1
    s.next=i+1
    temp.append(s.data)
    temp.append(s.next)
    place.append(temp)

tem1=[]
s.data=n;
s.next=0;
tem1.append(s.data)
tem1.append(s.next)
place.append(tem1)  #串列尾指向串列頭形成一個環狀鏈結串列
count=0
current=0
pre=0
i=0  #紀錄爆炸次數的變數,並事先歸零
while i<k:
    count=count+1   #計數器
    if (count==m):
        #從環狀串列中刪除這個號碼的位置
        place[pre][1]=place[current][1]
        count=0  #計數器歸零
        n=n-1	#剩下玩遊戲的人的總數少1
        i=i+1  #爆炸次數累加1
    pre=current
    current=place[current][1]
print("%d" %place[current][0])