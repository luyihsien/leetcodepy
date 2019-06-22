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
        tmp = n#保留目前的n而不是n開始被往下扣以後
        print('init tmp=',tmp)
        record = []
        print('init record=',record)
        while n > 0:
            print('nums[n]',nums[n],'nums[n-1]',nums[n-1])
            if nums[n] > nums[n - 1]:
                k = 0
                record.append(nums[n])#why直接一直增元素??#他不是下方else的record
                print('record',record)
                min_val = record[k]
                print('min_val init=',min_val)
                print('nums[n-1](判與min_val)',nums[n-1])
                while min_val <= nums[n - 1]:
                    k += 1
                    print('k',k)
                    min_val = record[k]
                    print('min_val',min_val)
                index = tmp - k
                print('index',index)
                print('n-1',n-1)
                nums[n - 1], nums[index] = nums[index], nums[n - 1]
                print('nums[n-1]',nums[n-1],'nums[index]',nums[index])
                nums[n:] = nums[n:][::-1]
                print('nus[n:]',nums[n:])
                print('nums',nums)
                return
            else:#nums[n]<=nums[n-1]
                record.append(nums[n])
                print('else的record',record)
            n -= 1
        print('nums未reverse',nums)
        nums.reverse()#最大的那種，倒過來變最小
        print('nums',nums)
print(Solution().nextPermutation([1,2,3,2,1]))
print(Solution().nextPermutation([1,2,3,2,1,4]))
print(Solution().nextPermutation([4,3,2,1]))
print(Solution().nextPermutation([1,1,3,2,1]))
print(Solution().nextPermutation([1,1,4,3,2]))
record=[]
nums=[1,2,3,2,1]
n=len(nums)-1