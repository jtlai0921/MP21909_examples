fp=open("data2.txt","r") #開啟唯讀檔案 
hit_result=[0]*100
for i in range(9):
    temp=fp.readline().split()
    for j in range(1,int(temp[0])+1):
        '''
        接下來有 a 個字串（均為兩個字元），
	依序代表每次打擊的結果。
	資料之間均以一個空白字元隔開。
        '''
        if temp[j]=="FO" or temp[j]=="GO" or temp[j]=="SO":
            #如果打擊結果的字串"FO","GO","SO"三者之一,表示為出局則記錄為0
            hit_result[(j-1)*9+i]=0
        elif temp[j]=="1B": #如果1壘安打則記錄為1
            hit_result[(j-1)*9+i]=1
        elif temp[j]=="2B": #如果2壘安打則記錄為2
            hit_result[(j-1)*9+i]=2
        elif temp[j]=="3B": #如果3壘安打則記錄為3
            hit_result[(j-1)*9+i]=3
        else: #如果都不是上述情況,表示為HR,即全壘打則記錄為4
            hit_result[(j-1)*9+i]=4
base=[0]*3  #記錄壘包是否有人
how_many=0 #記錄還可以有多少人出局
out=0;score=0;now=0 #now表示讀取到第幾筆資訊，out判斷是否三出局
how_many=int(fp.readline())
while how_many>0:
    if(hit_result[now]==0):
        out+=1#出局
        #如果三出局，清空壘包
        if(out%3==0):
            out=0
            base[0]=0
            base[1]=0
            base[2]=0
        how_many-=1
    else:
        if hit_result[now]==4: #如果是全壘打
            for k in range(3):
                #壘上每有一人加一分，並清空壘包
                if(base[k]):
                    score+=1
                    base[k]=0
            #打擊者加一分
            score+=1
        elif hit_result[now]==1: #如果是一壘打
            #如果三壘有人加一分，並且每一壘推移一壘
            if(base[2]):score+=1
            base[2]=base[1]
            base[1]=base[0]
            base[0]=1#打擊者上1壘
        elif hit_result[now]==2: #如果是二壘打
            #如果二三壘有人加一分
            if(base[2]):score+=1
            if(base[1]):score+=1
            #一壘人推移到三壘
            base[2]=base[0]
            base[0]=0
            #打擊手上二壘
            base[1]=1
        elif hit_result[now]==3: #如果是三壘打
            #一二三壘上有人加分
            if(base[2]):score+=1
            if(base[1]):score+=1
            if(base[0]):score+=1
            base[1]=0
            base[0]=0
            #打擊手上三壘
            base[2]=1
    now+=1
print("%d" %score)
