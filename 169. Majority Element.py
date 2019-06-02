dict={1:2,3:4}
for i in dict:
    print(dict[i])


class Solution:
    def majorityElement(self, nums):
        dict = {}
        l = []
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for i in dict:
            l.append(dict[i])
        #print('l',l)
        m = max(l)
        #print('m',m)
        for k, v in dict.items():
            if v == m:
                #print('m',m)
                return k
print(Solution().majorityElement([3,3,4]))