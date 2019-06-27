class Solution:
    def nextPermutation(self, nums):
        n=-1
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                n=i-1
                break
        if n==-1:
            nums.reverse()
        else:
            for i in range(len(nums)-1,n,-1):
                if nums[n]<nums[i]:
                    nums[n],nums[i]=nums[i],nums[n]