class Solution:
    def longestWPI(self, hours):
        a=[0]*len(hours)
        c=[0]*len(hours)
        for i in range(len(hours)):
            if hours[i]>8:
                a[i]=1
        print(a)
        if a[0]==1:
            c[0]=1
        else:
            c[0]=0
        for i in range(1,len(a)):
            if a[i]==1:
                c[i]=c[i-1]+1
            else:
                c[i]=c[i-1]-1




print(Solution().longestWPI([9,9,6,0,6,6,9,9,9]))