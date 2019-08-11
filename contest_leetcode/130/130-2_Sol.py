print(1%-2,1%-2)#值介於0~-4
class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return "0"
        nums = []
        while N != 0:
            print('N',N)
            r = N % (-2)
            print('r',r)
            N //= (-2)
            print('N除以-2後',N)
            if r < 0:
                r += 2
                N += 1
                print('r','N',r,N)
            nums.append(r)
            print('nums',nums)
        return ''.join(map(str, nums[::-1]))
print(Solution().baseNeg2(18))
#print(Solution().baseNeg2(3))
#print(Solution().baseNeg2(4))
print(5//-2)#(-2*-3)-1=(-2*-2)+1
print(-2//-2)#
print(1//-2)
print(-1//-2)