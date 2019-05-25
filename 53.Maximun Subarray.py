
class Solution:
    def maxSubArray(self, nums):
        sum=float('-inf')
        for i in range(len(nums)):
            head=0
            for j in range(i,len(nums)):
                head+=nums[j]
                if head>sum:
                    sum=head
        return sum
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))#17 but正確答案為6
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        m = float('-inf')
        for i in range(n):
            s = 0
            for j in range(i, n):
                s = s + nums[j]
                print('s',s)
                print('先m',m)
                m = max(m, s)
                print('m',m)
        return m
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))#17 but正確答案為6
'''
