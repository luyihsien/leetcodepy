class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        n=len(A)
        for i in range(n-2):
            for j in range(i+1,n-1):
                if sum(A[:i+1])==sum(A[i+1:j+1]) and sum(A[i+1:j+1])==sum(A)-sum(A[:i+1])-sum(A[i+1:j+1]):
                    return True
        return False
