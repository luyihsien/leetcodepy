class Solution:
    def largestSumAfterKNegations(self, A, K: int) -> int:
        b=A.copy()
        b.sort()
        d={}
        for i in range(len(A)):
            d[A[i]]=i
        print(d)
        while k:
            if b[0]>=0:
                A[d[b[0]]=-A[d[b[0]]]
                k=k-1
            for i in b:
                if b<0:
                    A[d[i]]=-A[d[i]]
                    k=k-1
        return sum(A)