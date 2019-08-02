class Solution:
    def relativeSortArray(self, arr1, arr2):
        d={}
        for i in arr1:
            if i in arr2 and i in d:
                d[i]+=1
            elif i in arr2:
                d[i]=1
        a=[]
        for i in arr2:
            a.extend([i]*d[i])
        arr=[x for x in arr1 if x not in arr2]
        print(arr)
        arr.sort()
        print(arr)
        arr1=a+arr
        return arr1
print(Solution().relativeSortArray([28,6,22,8,44,17],[22,28,8,6]))
a=[4,3,2]
a.sort()