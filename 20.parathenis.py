class Solution:
    def isValid(self, s):
        dict={'(':[0,[]],'{':[0,[]],'[':[0,[]],')':[0,[]],'}':[0,[]],']':[0,[]]}
        a=[]
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]][0]=dict[s[i]][0]+1

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
'''

