class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 0:
            raise RuntimeError("illegal numRows.")
        if numRows == 1 or numRows >= len(s):
            return s
        step = numRows + numRows - 2#??#去頭去尾而numRows*2是因為來回折返
        c = ['' for i in range(numRows)]
        print('c',c)
        for i in range(len(s)) :
            mod = i % step
            print('step',step,'mod',mod)
            if mod < numRows :#注意:不是mod<step
                c[mod] += s[i]
                print('c[mod]',c[mod])
            else :
                c[step - mod] += s[i]#step-mod不超出座標值因為只是在
                print('c[{}]'.format(step-mod),c[step-mod])
            print('c',c)
        res = ''
        for i in c:
            res += i
            print('res',res)
        return res
print(Solution().convert(s = "LEETCODEISHIRING", numRows = 3))
print(Solution().convert(s = "LEETCODEISHIRING", numRows = 4))