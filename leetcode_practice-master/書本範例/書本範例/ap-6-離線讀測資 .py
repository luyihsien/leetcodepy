ipline=['3 5','1 2 3 4 5','2 4 6 8 10','3 6 9 12 15']
num=len(ipline)
iplist=[]
for i in range(num):
    list01=list(map(int,ipline[i].split()))
    print(list01)
    iplist.append(list01)
print(iplist)



