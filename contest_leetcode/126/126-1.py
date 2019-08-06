#hanshaohey 世界排名第2
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        lts='abcdefghijklmnopqrstuvwxyz'
        ans=[]
        for lt in lts:
            a=[]
            for s in A:
                a.append(s.count(lt))
                ans.extend(min(a)*[lt])
        return ans
print(Solution().commonChars(["bella","label","roller"]))
'''
['a', 'a', 'b', 'b', 'e', 'e', 'e', 'l', 'l', 'l', 'l', 'l', 'l']
'''