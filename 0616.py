class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        a=arr[:]
        n=len(a)

        l=[]
        for i in range(len(arr)-1):
            if arr[i]==0:
                l.append(i+1)
        print(l)
        for i in l:
            print(n)
            print(i)
            arr.insert(i,0)
        print(arr)
Solution().duplicateZeros([1,0,2,3,0,4,5,0])
