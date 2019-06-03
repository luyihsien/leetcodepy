#0603
class Solution:
    def removeDuplicates(self, nums):
        count=0
        idx=0
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[idx]=i-idx
                idx=i
            else:
                nums[i],nums[i-1]=0,0
        return max(nums)
'''
最后执行的输入：
[0,3,4]
IndexError: list index out of range
'''
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        count=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums.pop(i-1)
                count+=1
        return count
'''
IndexError: list index out of range
Line 7 in removeDuplicates (Solution.py)
'''
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        count=0
        for i in range(1,len(nums)):
            if nums[i-1]!=nums[i]:
                count+=1
        return count
print(Solution().removeDuplicates([1,1,2]))
'''
解答错误
显示详情 
输入
[1,1,2]
输出
[1]
预期结果
[1,2]
'''
class Solution():
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        count=0
        for i in range(len(nums)):
            if nums[count]!=nums[i]:
                count+=1
                nums[count]=nums[i]
        print(nums)
        return count+1
print(Solution().removeDuplicates([1,1,2]))