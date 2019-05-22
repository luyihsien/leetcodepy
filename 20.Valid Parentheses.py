class Solution:
    def isValid(self, s):
        dict={'(':[0,[]],'{':[0,[]],'[':[0,[]],')':[0,[]],'}':[0,[]],']':[0,[]]}
        a=[]
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]][0]=dict[s[i]][0]+1
#對稱型，一左立馬一右型，BUT兩個都有就掛了...
'''
class Solution:
    def isValid(self, s):
        dict = {'(': [0, 0], '{': [0, 0], '[': [0, 0], ')': [0, 0], '}': [0, 0], ']': [0, 0]}
        a = []
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]][0] = dict[s[i]][0] + 1
                dict[s[i]][1] = i
        if dict['('][0] == dict[')'][0] and dict['{'][0] == dict['}'][0] and dict['['][0] == dict[']'][0]:
            if dict['('][1] < dict[')'][1] and dict['{'][1] < dict['}'][1] and dict['{'][1] == dict['}'][1]
             return True
            else:
                return False
        else:
            return False
'''


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while '[]' in s or '()' in s or '{}' in s:
            s = s.replace('[]','').replace('()','').replace('{}','')#順序換掉沒差
        return len(s) == 0
