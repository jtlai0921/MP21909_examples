temp=input("請輸入三個整數，數值以空白分開 \n").split()
a=int(temp[0])
b=int(temp[1])
c=int(temp[2])
success=[0]*3
ans=''*20
if a>0:  a = 1
if b>0:  b = 1
if((a&b)==c):  success[0]=1
else: success[0]=0
if((a|b)==c):  success[1]=1
else: success[1]=0
if((a^b)==c):  success[2]=1
else: success[2]=0
if success[0]==1: print("AND")
if success[1]==1: print("OR")
if success[2]==1: print("XOR")
if success[0]==0 and success[1]==0 and success[2]==0:
    print("IMPOSSIBLE")
