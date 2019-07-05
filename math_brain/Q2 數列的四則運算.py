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