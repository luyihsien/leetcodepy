#error
class Solution:
    def removeElement(self, nums, val):
        for i in range(len(nums)):
            if nums[i]==val:
                print('座標'+str(i))
                print(nums[i])
                nums.remove(nums[i])
                print(nums)
            else:
                print('座標'+str(i))
                print(nums[i])
                print(nums)
        return len(nums)
print(Solution().removeElement([0,1,2,2,3,0,4,2],2))
'''
0
[0, 1, 2, 2, 3, 0, 4, 2]
1
[0, 1, 2, 2, 3, 0, 4, 2]
2
[0, 1, 2, 3, 0, 4, 2]
3
[0, 1, 2, 3, 0, 4, 2]
0
[0, 1, 2, 3, 0, 4, 2]
4
[0, 1, 2, 3, 0, 4, 2]
2
[0, 1, 3, 0, 4, 2]
6
'''
