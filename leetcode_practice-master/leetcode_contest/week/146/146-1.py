class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:
        d={}
        a=0
        for i in dominoes:
            i.sort()
            i=str(i)
            print(i)
            if i in d:
                d[str(i)]+=1
            else:
                d[str(i)]=0
        for i in d:
            a+=(1+d[i])*(d[i])//2
        return a


