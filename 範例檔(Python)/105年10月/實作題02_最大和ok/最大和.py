fp=open("data2.txt","r");
temp=fp.readline().split()
N=int(temp[0]) #N群數字 
M=int(temp[1]) #每群有M個正整數 
number=[]
for i in range(0, N):
    tem = fp.readline().split(' ')
    tem1 = []
    for j in range(0, M):
        tem1.append(int(tem[j]))
    number.append(tem1)
BIG=[]
for i in range(0, N):
    BIG.append(0)
for i in range(0, N):
    BIG[i]=int(number[i][0])
    for j in range(0, M):
        if int(number[i][j])>BIG[i]:
            BIG[i]=int(number[i][j])
total=0
for i in range(0, N): #求和
    total=total+BIG[i]
print(total)
#找整除者
flag='N'
for i in range(0, N):
    if(total % BIG[i]==0):
        flag='Y'
        print(BIG[i],end=' ')
if (flag=='N'): #如果找不到整除者, 則輸出-1
    print("-1 ")
