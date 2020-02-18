#第一行是一個正整數n，說明團體中人數。 
n=int(input())
'''
第二行依序是0 的好友編號、1 的好友編號、
……、N-1 的好友編號。共有N 個數字，
包含0 到N-1 的每個數字恰好出現一次，
數字間會有一個空白隔開。
'''
friend_NO=[]
temp=input().split()
for i in range(n):
    friend_NO.append(int(temp[i]))
visited=[]
for i in range(n):
    visited.append(0) #未探訪
i=0;
counter=0;  #紀錄小群組的個數
success='N'; #用來紀錄是否順利找到小群體 
#如果全部探訪完畢就離開迴圈 
while (success=='N'):
    head=i;#紀錄此小群體的頭 
    counter=counter+1;	#累加有多少個小群體
    while friend_NO[i]!=head and visited[i]==0:
        visited[i]=1 #設定已探訪
        i=friend_NO[i]	#繼續探訪他的好友
    #已經找到此群體的源頭 
    visited[i]=1	 #設定已探訪	
    success='Y'  #表示已順利找到小群體
    #依序找出沒有探訪，且不在已找到的群體中，從其開始探訪
    for i in range(n):
        if visited[i]==0:
            success='N'
            break
print("%d" %counter)
