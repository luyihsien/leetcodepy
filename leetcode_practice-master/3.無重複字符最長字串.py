class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s =='':
            return 0
        count_max = 1
        re = []
        for i in range(len(s)):#終止條件與re空不空無關
            print('s[i]',s[i])
            if s[i] in re:
                re = re[re.index(s[i])+1:]
                print('re(if)的',re)
                re.append(s[i])
                print('re(if)的append後', re)
            else:
                re.append(s[i])
                print('re(else)的',re)
                if len(re) > count_max:
                    count_max = len(re)
                    print('count_max',count_max)
        return count_max
print(Solution().lengthOfLongestSubstring('abcabcbb'))
#print(Solution().lengthOfLongestSubstring('abcabdbb'))
#print(Solution().lengthOfLongestSubstring('dabcde'))