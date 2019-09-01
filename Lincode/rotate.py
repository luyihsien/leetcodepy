class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        # write your code here
        n=len(s)
        s=s[n-offset:]+s[:n-offset]
        return s
print(Solution().rotateString("abcdefg",3))
class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        # write your code here
        class Solution:
            """
            @param str: An array of char
            @param offset: An integer
            @return: nothing
            """

            def rotateString(self, s, offset):
                # write your code here
                n = len(s)
                offset = offset % n
                print(s[n-offset]+ s[:n - offset])
                s[:] = s[n - offset:] + s[:n - offset]
                return s
print(Solution().rotateString("abcdefg",3))
print(sum([]))