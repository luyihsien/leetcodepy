#error
class Solution:
    def removeElement(self, nums, val):
        for i in nums:
            if i==val:
                print(i)
                nums.remove(i)
                print(nums)
            else:
                print(i)
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
