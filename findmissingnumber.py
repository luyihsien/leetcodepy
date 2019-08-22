import collections
class Solution():
    def findmissingnumber(self,l):
        d=collections.Counter()
        for i in range(len(l)-1):
            if d[(l[i+1]-l[i])]==0:
                d[l[i + 1] - l[i]] = [i]#存下與第i與i+1項差d 的i
            else:
                d[l[i + 1] -l[i]].append(i)
        c=[]
        for i in d:
            if len(d[i])==1:
                c.append(abs(d[i]))
        a=max(c)

print(Solution().findmissingnumber([2,4,6,8,10,14,16,18,20]))