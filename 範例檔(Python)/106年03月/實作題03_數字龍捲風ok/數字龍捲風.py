#方向向量， 其中 0代表左 、1代表上 、2代表右 、3代表下
direction=[[0,-1],[-1,0],[0,1],[1,0]]
fp=open("data2.txt","r")
n=int(fp.readline()) #輸入 第一行 是整數 N，N為奇數且不小於 3。
'''
紀錄移動方式的變數, 一個 0~3 的整數 代表起始方向， 
代表起始方向， 其中 0代表左 、1代表上 、2代表右 、3代表下 。
'''
dir=int(fp.readline())
data=[]
for i in range(n):
    list1=[]
    list1=fp.readline().split()
    data.append(list1)
step = 1
stepcounter = 0
counter = 1
row = n // 2
col = n // 2
print("%d" %int(data[row][col]),end='')
while counter < n * n:
    for i in range(step):
        row += direction[dir][0]
        col += direction[dir][1]
        print("%d" %int(data[row][col]),end='')
        counter=counter+1
        if counter==n*n:
            break
    if counter==n*n:
        break
    stepcounter=stepcounter+1
    if stepcounter % 2 == 0:
        step=step+1
    dir=dir+1
    dir=dir % 4
