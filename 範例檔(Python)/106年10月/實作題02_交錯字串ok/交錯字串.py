k=int(input("輸入 k 值(整數): ")) #輸入 k 值(整數)
strings=input("請輸入由大小寫組成的交錯字串: ")  #輸入交錯字串

'''
   Is_Pre_Lowercase變數功能說明:
   此變數是用來追蹤前一個字元是否為小寫,初設值為空值None
   如果前一字元為小寫,此變數的值為布林資料型態True
   如果前一字元為大寫,此變數的值為布林資料型態False
'''
Is_Pre_Lowercase=None

Upper_no = 0  #連續大寫的字元總數
Lower_no = 0  #連續小寫的字元總數
Alternating_len = 0  #目前交錯的字串長度,初設值為0
longest = 0  #最長交錯的子字串長度,初設值為0

#處理第一個字元的作法
if strings[0].isupper()==True: #假如第一個字母為大寫字母
    Is_Pre_Lowercase = False   #將記錄前一字元是否為小寫的變數設定為False
    Upper_no = 1  #設定記錄連續大寫的變數為1
    if k==1: #假如k值為1
        Alternating_len = 1 #將目前交錯的字串長度設定為1
        longest = 1 #將最長交錯的子字串長度設定為1
else: #否則第一個字母為小寫字母
    Is_Pre_Lowercase = True #將記錄前一字元是否為小寫的變數設定為True
    Lower_no = 1 #設定記錄連續小寫的變數為1
    if k==1: #假如k值為1
        Alternating_len = 1  #將目前交錯的字串長度設定為1
        longest = 1  #將最長交錯的子字串長度設定為1

#第2個以後的字元的作法
for i in range(1,len(strings)):
    #前一個字元是大寫,而且目前這個字元也是大寫
    if (Is_Pre_Lowercase==False and
        strings[i].isupper()==True): 
        Upper_no += 1 #將記錄連續大寫字元總數的變數加1
        Lower_no = 0  #將記錄連續小寫字元總數歸零
        if Upper_no==k: #假如記錄連續大寫字元總數等於題目給定k值
            Alternating_len += k #將記錄目前交錯的字串長度的變數值加上k
            longest = max(Alternating_len, longest)  #取較大值作為最長交錯的子字串長度
        if Upper_no>k: Alternating_len = k  #假如記錄連續大寫字元總數大於k值,超過的字元數不列入計算

    #前一個字元是小寫,但是目前這個字元是大寫
    elif (Is_Pre_Lowercase==True and
          strings[i].isupper()==True):
        if Lower_no<k: Alternating_len = 0 #假如連續小寫的字元總數小於k,則將目前交錯的字串長度數值歸零
        Upper_no = 1 #將記錄連續大寫字元總數設定為1
        Lower_no = 0 #將記錄連續小寫字元總數歸零
        if k==1: #假如k值為1
            Alternating_len += 1 #將目前交錯的字串長度加1
            longest = max(Alternating_len, longest) #取較大值作為最長交錯的子字串長度
        Is_Pre_Lowercase = False  #設定前一字元為大寫

    #前一個字元是小寫,而且目前這個字元也是小寫
    elif (Is_Pre_Lowercase==True and
          strings[i].islower()==True):
        Lower_no += 1 #將記錄連續小寫字元總數的變數加1
        Upper_no = 0  #將記錄連續大寫字元總數歸零
        if Lower_no==k: #假如記錄連續小寫字元總數等於題目給定k值
            Alternating_len += k #將記錄目前交錯的字串長度的變數值加上k值
            longest = max(Alternating_len, longest) #取較大值作為最長交錯的子字串長度
        if Lower_no>k: Alternating_len = k #假如記錄連續大寫字元總數大於k值,超過部分不列入計算

    #前一個字元是大寫,但是目前這個字元是小寫
    elif (Is_Pre_Lowercase==False and
          strings[i].islower()==True):
        if Upper_no<k:  Alternating_len = 0 #假如連續大寫的字元總數小於k,則將目前交錯的字串長度數值歸零
        Lower_no = 1 #將記錄連續小寫字元總數設定為1
        Upper_no = 0 #將記錄連續大寫字元總數歸零
        if k==1: #假如k值為1
            Alternating_len += 1 #將目前交錯的字串長度加1
            longest = max(Alternating_len, longest) #取較大值作為最長交錯的子字串長度
        Is_Pre_Lowercase = True #設定前一字元為小寫

print("%d" %longest)#輸出輸入字串中滿足 k-交錯字串的要求的最長一段連續子字串的長度
