class Solution:
    def largestSumAfterKNegations(self, A, K: int) -> int:
        b=A.copy()
        b.sort()
        d={}
        for i in range(len(A)):
            d[A[i]]=i
        print(d)
        while K:
            if b[0]>=0:
                K=K-1
                A[d[b[0]]]=-A[d[b[0]]]
                print('A',A)
            for i in b:
                if i<0:
                    A[d[i]]=-A[d[i]]
                    K=K-1
                    print('A',A)
                    if K==0:
                        break
        return sum(A)

print(Solution().largestSumAfterKNegations([4,2,3],1))
print(Solution().largestSumAfterKNegations(A = [3,-1,0,2], K = 3))
print(Solution().largestSumAfterKNegations(A = [2,-3,-1,5,-4], K = 2))
print(Solution().largestSumAfterKNegations([-2,5,0,2,-2],3))
"""
A [-2, 5, 0, 2, 2]
A [-2, 5, 0, 2, -2]
A [-2, 5, 0, 2, 2]
7
預期11
"""