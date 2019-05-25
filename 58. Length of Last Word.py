#a='a' a.split(' ')[-1]#a.split為list
# #IndexError: list index out of range
class Solution:
    def lengthOfLastWord(self, s):
        b=s.split()[-1]
        print(b)
        return len(b)
print(Solution().lengthOfLastWord("a "))
class Solution:#正確解法
    def lengthOfLastWord(self, s: str) -> int:
        string = s.split()
        print(string)
        if not string:#
            return 0#為何要加此二列??
        return len(string[-1])
print(Solution().lengthOfLastWord("a "))
