class Solution:
    def bitwiseComplement(self, N: int) -> int:
        n=2^(len(bin(N)[2:]))-1
        print(len(bin(N)[2:]))
        print(n)
Solution().bitwiseComplement(5)