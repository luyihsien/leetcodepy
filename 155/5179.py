class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        d={}
        n=len(arr)
        l=[]
        m=float('inf')
        for i in range(n-1):
            if arr[i+1]-arr[i]<m:
                m=arr[i+1]-arr[i]
            d[arr[i],arr[i+1]]=arr[i+1]-arr[i]
        for i in d:
            if d[i]==m:
                l.append(list(i))
        l.sort()
        return l
print(Solution().minimumAbsDifference([1,3,6,10,15]))

