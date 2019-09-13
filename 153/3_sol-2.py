class Solution:
    def maximumSum(self, arr) -> int:
        n = len(arr)
        max_ending_here0 = n * [arr[0]]  # no deletion
        print('max_ending_here0', max_ending_here0)
        max_ending_here1 = n * [arr[0]]  # at most 1 deletion
        print('max_ending_here1', max_ending_here1)
        for i in range(1, n):
            max_ending_here0[i] = max(max_ending_here0[i - 1] + arr[i], arr[i])
            print('max_ending_here0',max_ending_here0)
            max_ending_here1[i] = max(max_ending_here1[i - 1] + arr[i], arr[i])
            print('max_ending_here1',max_ending_here1)
            if i >= 2:
                max_ending_here1[i] = max(max_ending_here1[i], max_ending_here0[i - 2] + arr[i])
                print('max_ending_here1', max_ending_here1)
        return max(max_ending_here1)
print(Solution().maximumSum(arr = [1,-2,0,3]))
