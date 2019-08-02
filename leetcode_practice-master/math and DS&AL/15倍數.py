#Sol 1
l=[]
for i in range(1,16):
    if i%3!=0 and i%5!=0 or i%15==0:
        l.append(i)
print(l)
#Sol 2
print([i for i in range(1,16) if i%3!=0 and i%5!=0 or i%15==0])
print([i for i in range(1,16) if not (i%3==0 or i%5==0) or i%15==0])
