num=[9,6,1,6,2]
for i in range(0,len(num)-2,2):
    print(i)
print(num)

class Solution:
    def movesToMakeZigzag(self, nums: 'List[int]') -> int:
        n=0
        for i in range(0,len(nums)-2,2):
            if nums[i+1]>=nums[i] and nums[i+1]<=nums[i+2]:
                while nums[i+1]<=nums[i+2]:
                    nums[i+2]=nums[i+2]-1
                    n=n+1
            if nums[i + 1] <= nums[i] and nums[i + 1] >= nums[i + 2]:
                while nums[i + 1] <= nums[i]:
                    nums[i] = nums[i] - 1
                    n = n + 1
        return n
Solution.movesToMakeZigzag([7,4,8,9,7,7,5])


