class Solution:
    def singleNumber(self, nums):
        nums.sort()
        for i in nums:
            if nums[i]==nums[i+1]
class Solution:
    def singleNumber(self, nums):
        while len(nums) > 1:
            a = max(nums)
            nums.remove(a)
            b = max(nums)
            nums.remove(b)
            if a != b:
                if b in nums:
                    return b
                else:
                    return a
        return nums[0]
class Solution:
    def singleNumber(self, nums):
        while len(nums)>1:
            a=max(nums)
            nums.remove(a)
            b=max(nums)
            nums.remove(b)
            if a!=b:
                if b in nums:
                    return a
                else:
                    return b
        return nums[0]

'''
超出时间限制
'''
class Solution:#正解1
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for num in nums:
            a = a ^ num
        return a
class Solution:#正解2
    def singleNumber(self, nums):
        ## 解法一 利用set的唯一性
        return sum(set(nums)) * 2 - sum(nums)