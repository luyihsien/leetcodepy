class Solution:
    def romanToInt(self, s):
        n_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, "C": 100, "D": 500, 'M': 1000}
        result = 0
        for i in range(len(s)):
            if i > 0 and n_map[s[i]] > n_map[s[i - 1]]:
                # if n_map[s[i]]>n_map[s[i-1]]:
                result += n_map[s[i]] - 2 * n_map[s[i - 1]]
            else:
                result += n_map[s[i]]
        return result
