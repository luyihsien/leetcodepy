class Solution:
    def largestUniqueNumber(self, A) -> int:
        if A==[]:
            return -1
        A.sort()
        d={}
        for i in A:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        print(d)
        while 1:
            if A==[]:
                return -1
            elif d[max(A)]!=1:
                A=A[:len(A)-d[max(A)]]
            else:
                return max(A)
print(Solution().largestUniqueNumber([9,9,8,8]))
print(Solution().largestUniqueNumber([5,7,3,9,4,9,8,3,1]))