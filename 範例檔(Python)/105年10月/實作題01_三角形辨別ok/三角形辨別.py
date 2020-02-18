while True:
    in1 = input('請輸入三角形三邊長 (按q結束程式): ')
    if in1 == 'q': break
    temp=in1.split()
    a=int(temp[0])
    b=int(temp[1])
    c=int(temp[2])

    #比較三邊以a,b,c由小到大排序
    if a>b: t=a;a=b;b=t 
    if b>c: t=b;b=c;c=t 
    if a>b: t=a;a=b;b=t	
    
    print("%d %d %d " %(a,b,c))
    if a+b<=c:  #無法形成三角形
        print("No")
        continue;
    ab=a*a+b*b
    cc=c*c
    if ab>cc:
        print("Acute")
    elif ab==cc:
        print("Right")
    else:
        print("Obtuse")
