'''
5064. 删除字符串中的所有相邻重复项  显示英文描述  
用户通过次数 255
用户尝试次数 302
通过次数 256
提交次数 483
题目难度 Easy
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。

在 S 上反复执行重复项删除操作，直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
'''
'''
class Solution:
    def removeDuplicates(self, S: str) -> str:
'''
a=''
a.join(['1','2','3'])#TypeError: sequence item 0: expected str instance, int found
print(a.join(['1','2','3']))
'''
class Solution:
    def removeDuplicates(self, S):
        list=[]
        for i in S:
            list.append(i)
        a=''
        while 1:
            for i in range(len(list)):
                if list[i]==list[i+1]:
                    list.remove(list[i])
                    list.remove(list[i+1])
                else:
                    break
        return a.join(list)
'''


class Solution:
    def removeDuplicates(self, S):
        list = []
        for i in S:
            list.append(i)
        a = ''
        b = 2
        c = 1
        while b > c:
            b = len(list)
            print(b)
            for i in range(len(list)):
                if list[i] == list[i-1]:
                    list.remove(list[i])
                    list.remove(list[i-1])
                    print(list)
                c = len(list)
                print(c)

        return a.join(list)
Solution().removeDuplicates("abbaca")