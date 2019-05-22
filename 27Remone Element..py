#error
b=6
for i in range(b):#寫下去時b就已經定了，不會跟著改
    print(b-2)
    b=b-2
#4 2 0 -2 -4 -6#還是原來的6次
class Solution:
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)







print(Solution().removeElement([0,1,2,2,3,0,4,2],2))#無論刪的是不是自己，接往下一個走了
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
