class Solution(object):
    def longestOnes(self, A, k):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        res = zero = l = 0

        for h in range(len(A)):
            print('res',res,'zero',zero,'l',l,'h',h,'k',k)
            if A[h] == 0:
                zero += 1
                print('zero',zero)
            while zero > k:
                if A[l] == 0:
                    zero -= 1
                    print('zero',zero)
                l += 1
                print('l',l)
            print('h-l+1',h-l+1)
            res = max(res, h-l+1)
            print('res',res)
        return res
print(Solution().longestOnes(A = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
