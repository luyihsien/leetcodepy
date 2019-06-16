class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        n=len(arr)
        l=[]
        for i in range(len(arr)-1):
            if arr[i]==0:
                l.append(i+1)
        for i in l:
            arr.insert(i,0)
        arr=arr[:n]
        print(arr)
Solution().duplicateZeros([1,0,2,3,0,4,5,0])
