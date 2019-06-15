a=[[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
a.sort(reverse = True)
print(a)
count=0
b=a[0][0]
c=0
for i in range(len(a)):
    if a[i][0]==b and count<=5:
        a[c][1]+=a[i][0]
        count=count+1
    else:
        count=1
        c=c+1






