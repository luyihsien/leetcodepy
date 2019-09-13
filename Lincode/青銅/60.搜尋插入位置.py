class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """

    def searchInsert(self, A, target):
        m = max(A)#A有值的時候才有，不然會error
        n = len(A)
        if target > m:
            return n
        for i in range(n):
            if A[i] >= target:
                return i
#sum(),max(),min()內至少要有一參數
print(sum([]))#0
print(max([]))#error
class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        if len(A)==0:
            return 0
        n=len(A)
        if target>max(A):
            return n
        for i in range(n):
            if A[i]>=target:
                return i
        # write your code here
