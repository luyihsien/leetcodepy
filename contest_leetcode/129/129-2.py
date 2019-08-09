''''
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        c = 0
        a = 1
        while 1:
            print(10**len(str(a)))
            if a % K == 0:
                return len(str(a))
            print(len(str(a)))
            print('10 ** (len(str(a)))={}'.format((10 ** (len(str(a))))))
            if (10 ** (len(str(a)))) % K == 0:
                return -1
            a = a * 10 + 1
            c+=1
            if c==7:
                break

print(Solution().smallestRepunitDivByK(3))
print(Solution().smallestRepunitDivByK(6))
'''

print(10%6)
print(100%6)
print(110%6)
print(1%6)
print(11%6)
print(111%6)
print(1111%6)