'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须原地修改，只允许使用额外常数空间。
以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def nextPermutation(self, nums) -> None:
        n = len(nums) - 1#座標
        print('init n=',n)
        tmp = n
        print('init tmp=',tmp)
        record = []
        print('init record=',record)
        while n > 0:
            if nums[n] > nums[n - 1]:
                k = 0
                record.append(nums[n])
                print('record',record)
                min_val = record[k]
                print('min_val init=',min_val)
                while min_val <= nums[n - 1]:
                    k += 1
                    print('k min',k)
                    min_val = record[k]
                    print('min_val',min_val)
                index = tmp - k
                print('index',index)
                nums[n - 1], nums[index] = nums[index], nums[n - 1]
                print('nums[n-1]',nums[n-1],'nums[inedx]',nums[index])
                nums[n:] = nums[n:][::-1]
                print('nums',nums)
                return
            else:
                record.append(nums[n])
                print('record',record)
            n -= 1
        nums.reverse()
        print('nums',nums)
print(Solution().nextPermutation([1,2,3,2,1]))