class Solution(object):
    def generate(self, numRows):
        ret = []
        for i in range(numRows):
            tmp = [0] * (i + 1)
            print('首尾未含1 tmp',tmp)
            tmp[0], tmp[-1] = 1, 1
            ret.append(tmp)
            print('ret',ret)
        for i in range(2, len(ret)):
            for j in range(1, len(ret[i]) - 1):
                ret[i][j] = ret[i - 1][j - 1] + ret[i - 1][j]
                print('ret',ret)
        return ret
Solution().generate(5)