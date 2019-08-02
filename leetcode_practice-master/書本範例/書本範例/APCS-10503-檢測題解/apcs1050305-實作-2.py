# 1050305APCS實作題---題二

line=input("請輸入列,行,方法：").split(" ")
R=int(line[0]);C=int(line[1]);way=int(line[2])


#輸入矩陣------------------------
X=[[0,0],
   [0,0],
   [0,0]]
for i in range(3):
    j=0
    X[i][j],X[i][j+1]=input("請輸入矩陣內容").split(" ")
    X[i][j]=int(X[i][j])
    X[i][j+1]=int(X[i][j+1])
#---------------------------------
mk=input("輸入方法").split(" ")
for i in range(len(mk)):
    print(mk[i],end=" ")
#---------------------------------


for k in range(len(mk)):
    if mk[k]==0:
        #旋轉rotate(X)     mk=0
        if len(X)==3:
            result = [[0,0,0],
                        [0,0,0]]
            for i in range(len(X)):
                for j in range(len(X[0])):
                    result[j][i] = X[i][j]
        else:
            result = [[0,0],
                        [0,0],
                        [0,0]]
            for i in range(len(X)):
                for j in range(len(X[0])):
                    result[j][i] = X[i][j]
     
    else:
        #翻轉flip(X)       mk=1
        if len(X)==2:
            result = [[0,0,0],
                      [0,0,0]]
            for i in range(len(X)):
                for j in range(len(X[0])):
                    result[i][j]= X[3-i][j]
        else:
            result = [[0,0],
                      [0,0],
                      [0,0]]
            for i in range(len(X)):
                for j in range(len(X[0])):
                    result[i][j]= X[2-i][j]



for r in X:
    print("原X=",r)


for r in result:
    print("  新Y=",r)






