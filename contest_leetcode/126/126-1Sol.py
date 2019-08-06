'''
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
            print()
            num=min([s.count(lt) for s in A])
            ans.extend([lt]*num)
            print('ans',ans)
        return ans
Solution().commonChars(["bella","label","roller"])
'''
a=[2]
a.extend([3]*0)
#print(a)
#print([2]*0)
a.append('a'*0)
print(a)