op=['*','+','-','/','']
d=['*','+','-','/']
for i in range(100,1000):
    i1=str(i)
    for j in range(len(op)):
        print(op[j])
        for k in range(len(op)):
            val=i1[2]+op[j]+i1[1]+op[k]+i1[0]
            l=[]
            for k in range(len(val)):
                if val[k] in d:
                    l.append(k)

            val1=eval(val)
            if len(val)>3:
                if i==val1:
                    print(i)
#https://zhuanlan.zhihu.com/p/37525980
operator = ['','*']
for i in range(1000,10000):
    # 末尾数字不为0
    if(i % 10 == 0): continue
    # 将四位数转为各个数字的序列
    numList = list(str(i))
    for l in range(len(operator)):
        for m in range(len(operator)):
            for r in range(len(operator)):
                # 如果操作符不为''，其后的数字不为'0'
                if(operator[l]!='' and numList[1]=='0') or\
                (operator[m]!='' and numList[2]=='0'):
                    continue
                # 组合算式
                formulaStr = numList[0]+operator[l]+numList[1]+operator[m]\
                +numList[2]+operator[r]+numList[3]
                if(len(formulaStr)>4):# 一定要插入1个运算符
                    # 如果算式结果等于逆序排列后的数，输出结果
                    if(eval(formulaStr)==int(str(i)[::-1])):
                        print(str(i)+" ---> "+formulaStr+"="+str(i)[::-1])