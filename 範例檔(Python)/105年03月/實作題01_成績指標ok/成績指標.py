while True:
    n1=input("請輸入學生人數: ")
    if n1 == '': break
    n=int(n1)
    num = []
    in2=input("請輸入學生成績: ")
    temp = in2.split(' ')
    for i in range(0, n):
        num.append(int(temp[i]))
    num.sort()#將成績進行排序
    for i in range(n):
        print("%d " %num[i], end='')
    print()
    if num[0]>=60:
        print("best case ")#如果全部分數都大於60,表示最佳狀況 
        print("%d " %num[0])#印出最低及格分數 
    elif num[n-1]<60:
        print("%d " %num[n-1])#印出最高不及格分數 
        print("worst case ") #如果全部分數都小於60,表示最差狀況 
    else :
        for i in range(n-1,-1,-1):
            if num[i] <60:
                print("%d" %num[i])
                break
        for i in range(n):
            if num[i] >=60:
                print("%d" %num[i])
                break
