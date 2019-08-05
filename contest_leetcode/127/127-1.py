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
                print(b[0])
                print(d[b[0]])
                print(A[d[b[0]]])
                K=K-1
                '''
                A[d[b[0]]=-A[d[b[0]]]
                k=k-1
            for i in b:
                if i<0:
                    A[d[i]]=-A[d[i]]
                    k=k-1
        return sum(A)
        '''

Solution().largestSumAfterKNegations([4,2,3],1)