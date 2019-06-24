import random

count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
count=[0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#while 0 in count:
    #count.remove(0)
nsample=random.randint(1,len(count)+1)
count=random.sample(count,nsample)
print(count)
mx=max(count)
mn=min(count)
av=0
most=0
for i in count:
    av+=i
av=av/len(count)
d={}
l=[]
a=0
for i in count:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for k in d:
    l.append(d[k])
a=max(l)

for k,v in d.items():
    if v==a:
        most=k
        break
mid=0
count.sort()
if len(count)%2==0:
    mid=(count[len(count)//2]+count[(len(count)//2)-1])/2
else:
    mid=count[len(count)//2]
#if mid
print([float(mn),float(mx),float(av),float(mid),float(most)])

'''
class Solution:
    def sampleStats(self, count):
'''
class Solution:
    def sampleStats(self, count):
        nsample=random.randint(1,len(count)+1)
        count=random.sample(count,nsample)
        mx=max(count)
        mn=min(count)
        av=0
        most=0
        for i in count:
            av+=i
        av=av/len(count)
        d={}
        l=[]
        a=0
        for i in count:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for k in d:
            l.append(d[k])
        a=max(l)
        for k,v in d.items():
            if v==a:
                most=k
                break
        mid=0
        count.sort()
        if len(count)%2==0:
            mid=(count[len(count)//2]+(count[((len(count)//2)-1)])/2)
        else:
            mid=count[len(count)//2]
        return [float(mn),float(mx),float(av),float(mid),float(most)]