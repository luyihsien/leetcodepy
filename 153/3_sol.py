class Solution:
    def maximumSum(self, arr) -> int:
        mwc = []
        ms = []
        r = max(arr)
        if r < 0:
            return r
        for n in arr:
            if not mwc:
                mwc.append(n)
                print('mwc',mwc)
                ms.append(0)
                print('ms',ms)
            else:
                ms.append(max(ms[-1] + n, mwc[-1]))
                mwc.append(max(n, n + mwc[-1]))

                print('mwc',mwc,'ms',ms)
                r = max([r, ms[-1], mwc[-1]])
        return r
print(Solution().maximumSum(arr = [1,-2,0,3]))