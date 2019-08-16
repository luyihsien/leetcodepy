class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        l = []
        v = 0
        c = 0

        for i in range(len(S)):
            if S[i] == '(':
                c += 1
            if S[i] == ')':
                c -= 1
            if c == 0:
                l.append(S[v + 1:i])
                v = i + 1
        return ''.join(l)
print(Solution().removeOuterParentheses('((()()))(())'))
print(Solution().removeOuterParentheses('(())()(()(()))'))
print(Solution().removeOuterParentheses('((()()))((()))'))