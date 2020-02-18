fp=open("data2.txt","r")
N=int(fp.readline())
data = []
for i in range(0, N):
    tem=fp.readline().split(' ')
    tlist=[]
    for j in range(0, 2):
        tlist.append(int(tem[j]))
    data.append(tlist)

data.sort(key=lambda x:x[0])  #依照第一個數遞增排序
ans = data[0][1] - data[0][0]  #第一個線段長度
for i in range(1, N):  #從第2個線段開始處理
    if (data[i][0]>data[i-1][1]):  #獨立線段,未重疊
        ans = ans + data[i][1] - data[i][0]
    elif (data[i][0]<=data[i-1][1])and (data[i][1]<=data[i-1][1]):  #此線段在前一線段中
        data[i][0] = data[i-1][0]
        data[i][1] = data[i-1][1]
    elif (data[i][0]<=data[i-1][1]) and (data[i][1]>data[i-1][1]):  #此線段與前一線段重疊
        ans = ans + data[i][1] - data[i-1][1]

print(ans)
