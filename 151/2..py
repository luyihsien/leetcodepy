import collections
class Solution:
    def invalidTransactions(self, transactions):
        res=[]
        c=collections.Counter()
        for i in transactions:
            j=i.split(',')
            if int(j[2])>1000:
                res.append(i)
                continue
            if c[j[0]]==0:
                c[j[0]]=[j[1]]
            if c[j[0]]!=0:
                for _ in c[j[0]]:
                    if abs(int(_ )-int(j[1]))<=60:
                        res.append(i)
            c[j[0]].append(j[1])
        return res



