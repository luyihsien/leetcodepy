class Solution:
    def balancedStringSplit(self, s: str) -> int:
        a = 1
        d = {'L': 'R', 'R': 'L'}
        S = [s[0]]
        n = len(s)
        for i in range(1, n):

            if S == []:
                a += 1
                S.append(s[i])
            elif S[-1] == d[s[i]]:
                S.pop()
            else:
                S.append(s[i])
        return a
print(Solution().balancedStringSplit(s = "RLRRLLRLRL"))