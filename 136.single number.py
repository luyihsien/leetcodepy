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