#題目是順時針方向旋轉時，所以逆時針方向旋轉就會恢復原狀
def counterclockwise(mat):  
    temp_matrix = []  #回傳串列
    row = len(mat)  
    col = len(mat[0])  
    for i in range(col-1, -1, -1):
        temp = []
        for j in range(0, row):  #原來的最後行成為第一列
            temp.append(mat[j][i])
        temp_matrix.append(temp)
    return temp_matrix

def turn(mat):  #翻轉
    temp_matrix = []
    row = len(mat)
    for i in range(row-1, -1, -1):  #將最後列成為第一列
        temp_matrix.append(mat[i])
    return temp_matrix

temp = input().split(' ')
R = int(temp[0])
C = int(temp[1])
M = int(temp[2])
matrix = []
for i in range(0, R):
    temp = input().split(' ')
    tlist = []
    for j in range(0, C):
        tlist.append(temp[j])
    matrix.append(tlist)
temp = input().split(' ')
for i in range(M-1,-1,-1): #反向操作
    if temp[i] == '1':  templist = turn(matrix)  #翻轉
    else:   templist = counterclockwise(matrix)  #旋轉
    matrix = templist[:]  #將回傳串列複製給matrix串列
    
#顯示解答
row = len(matrix) #列數
col = len(matrix[0]) #行數
print(row, col)
for i in range(0, row):
    for j in range(0, col):
        if j == col-1:  print("%s" %matrix[i][j])
        else:  print("%s" %matrix[i][j], end=' ')