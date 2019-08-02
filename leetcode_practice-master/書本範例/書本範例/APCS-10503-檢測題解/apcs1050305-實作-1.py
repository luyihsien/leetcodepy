# 1050305APCS實作題---題一

#輸入---------------
stu_num=int(input("請輸入學生人數："))
scores=[]
inscore=0   
while(stu_num > 0):
    inscore=int(input("請依序輸入學生成績："))    
    if (stu_num > 0):
        scores.append(inscore)

    stu_num -= 1

#處理----------------    
scores.sort()
for i in range(len(scores)):
    print(scores[i],end=" ")
print()

worst=best= -1
for j in range(len(scores)):
    if (scores[j] >= 60 and worst==-1): worst=scores[j]
    if (scores[j] < 60): best=scores[j]

#輸出-----------------    
if (best==-1):
    print("best case")
else:
    print(best)
if (worst==-1):
    print("worst case")
else: print(worst)
