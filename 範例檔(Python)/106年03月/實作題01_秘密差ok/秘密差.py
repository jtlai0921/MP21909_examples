X=input("請輸入位數不超過1000位的正整數:")
odd = 0; even=0
if (len(X) % 2) !=0:  #若數字總長度不能被2整除 ,表示第一個字元是奇位數
    for i in range(len(X)):
        if i%2 ==0: odd += (int)(X[i]); #奇數位數字加總 
        else: even += (int)(X[i]);  #偶數位數字加總
else:
    for i in range(len(X)):
        if i%2 ==0: even += (int)(X[i]); #偶數位數字加總
        else: odd += (int)(X[i]); #奇數位數字加總
print("%d" %abs(odd-even))