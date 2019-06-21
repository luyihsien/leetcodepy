class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0
        for i in range(len(s)):
            odd = self.mid_expand(s, i, i)
            print('odd=',odd)
            even = self.mid_expand(s, i, i + 1)
            print('even=',even)
            m = max(odd, even)
            print('m',m)
            if m > right - left:
                left = i - (m - 1) // 2
                right = i + m // 2
            print('s[left:right + 1]=',s[left:right + 1])
        return s[left:right + 1]

    def mid_expand(self, s, left, right):
        print('left init=',left,'right init=',right)
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            print('left=',left,'right=',right)
        print('right - left - 1 =',right - left - 1)
        return right - left - 1
Solution().longestPalindrome('abccba')