class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        count=0
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                count+=1
                nums[count]=nums[i]
        return count+1
'''
成功
显示详情
执行用时 : 76 ms, 在Remove Duplicates from Sorted Array的Python3提交中击败了94.41% 的用户
内存消耗 : 14.7 MB, 在Remove Duplicates from Sorted Array的Python3提交中击败了83.47% 的用户
'''
print(Solution().removeDuplicates([3]))#若長度是1 range(1,1) 故連進去range都不會進去。
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        count=0
        for i in range(1,len(nums)):
            if nums[count]!=nums[i]:
                count+=1
                nums[count]=nums[i]
        return count+1
'''
成功
显示详情 
执行用时 : 68 ms, 在Remove Duplicates from Sorted Array的Python3提交中击败了98.65% 的用户
内存消耗 : 14.6 MB, 在Remove Duplicates from Sorted Array的Python3提交中击败了95.70% 的用户
'''