''''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
'''
class Solution:
    def searchInsert(self, nums, target):
        if len(nums)==0:
            return 0
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        for i in range(1,len(nums)):
            if nums[i]>target and nums[i-1]<target:
                return i
        if max(nums)<target:
            return len(nums)
        if min(nums)>target:
            return 0

'''
成功
显示详情 
执行用时 : 52 ms, 在Search Insert Position的Python3提交中击败了90.74% 的用户
内存消耗 : 13.5 MB, 在Search Insert Position的Python3提交中击败了96.03% 的用户
'''
