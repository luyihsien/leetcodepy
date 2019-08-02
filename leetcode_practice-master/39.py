'''''
class Solution:
    def combinationSum(self, candidates, target: int) :
        candidates.sort()
        print('candidates',candidates)
        n = len(candidates)
        res = []#公用list，函數路徑下皆傳入
        def helper(i, tmp_sum, tmp):
            print('i', i, 'tmp_sum', tmp_sum,'tmp',tmp,'target',target)
            if tmp_sum > target or i == n:#i==n時表示超出座標範圍了，i確保在無論任何list長度，可以知道目前驗到哪裡
                return#沒有東西需要回傳but也表示子問題已解決
            if tmp_sum == target:
                print('i',i,'tmp_sum',tmp_sum)
                res.append(tmp)
                print('res',res)
                return
            #print('helper(i,  tmp_sum + candidates[i],tmp + [candidates[i]])',helper(i,  tmp_sum + candidates[i],tmp + [candidates[i]]))
            helper(i,  tmp_sum + candidates[i],tmp + [candidates[i]])#參數不只用在內部計算時，也可又被拿來變成內部函數的參數(參i用法)#list不只增添在內部計算而已，也可操作在內部函數的參數
            #print('helper(i+1, tmp_sum ,tmp)',helper(i+1, tmp_sum ,tmp))
            helper(i+1, tmp_sum ,tmp)
        helper(0, 0, [])
        return res
print(Solution().combinationSum([],2))
print(Solution().combinationSum([7,6,3,2],7))
'''

'''
candidates [2, 3, 6, 7]
i 0 tmp_sum 0 tmp [] target 7
i 0 tmp_sum 2 tmp [2] target 7
i 0 tmp_sum 4 tmp [2, 2] target 7
i 0 tmp_sum 6 tmp [2, 2, 2] target 7
i 0 tmp_sum 8 tmp [2, 2, 2, 2] target 7
i 1 tmp_sum 6 tmp [2, 2, 2] target 7
i 1 tmp_sum 9 tmp [2, 2, 2, 3] target 7
i 2 tmp_sum 6 tmp [2, 2, 2] target 7
i 2 tmp_sum 12 tmp [2, 2, 2, 6] target 7
i 3 tmp_sum 6 tmp [2, 2, 2] target 7
i 3 tmp_sum 13 tmp [2, 2, 2, 7] target 7
i 4 tmp_sum 6 tmp [2, 2, 2] target 7
i 1 tmp_sum 4 tmp [2, 2] target 7
i 1 tmp_sum 7 tmp [2, 2, 3] target 7
i 1 tmp_sum 7
res [[2, 2, 3]]
i 2 tmp_sum 4 tmp [2, 2] target 7
i 2 tmp_sum 10 tmp [2, 2, 6] target 7
i 3 tmp_sum 4 tmp [2, 2] target 7
i 3 tmp_sum 11 tmp [2, 2, 7] target 7
i 4 tmp_sum 4 tmp [2, 2] target 7
i 1 tmp_sum 2 tmp [2] target 7
i 1 tmp_sum 5 tmp [2, 3] target 7
i 1 tmp_sum 8 tmp [2, 3, 3] target 7
i 2 tmp_sum 5 tmp [2, 3] target 7
i 2 tmp_sum 11 tmp [2, 3, 6] target 7
i 3 tmp_sum 5 tmp [2, 3] target 7
i 3 tmp_sum 12 tmp [2, 3, 7] target 7
i 4 tmp_sum 5 tmp [2, 3] target 7
i 2 tmp_sum 2 tmp [2] target 7
i 2 tmp_sum 8 tmp [2, 6] target 7
i 3 tmp_sum 2 tmp [2] target 7
i 3 tmp_sum 9 tmp [2, 7] target 7
i 4 tmp_sum 2 tmp [2] target 7
i 1 tmp_sum 0 tmp [] target 7
i 1 tmp_sum 3 tmp [3] target 7
i 1 tmp_sum 6 tmp [3, 3] target 7
i 1 tmp_sum 9 tmp [3, 3, 3] target 7
i 2 tmp_sum 6 tmp [3, 3] target 7
i 2 tmp_sum 12 tmp [3, 3, 6] target 7
i 3 tmp_sum 6 tmp [3, 3] target 7
i 3 tmp_sum 13 tmp [3, 3, 7] target 7
i 4 tmp_sum 6 tmp [3, 3] target 7
i 2 tmp_sum 3 tmp [3] target 7
i 2 tmp_sum 9 tmp [3, 6] target 7
i 3 tmp_sum 3 tmp [3] target 7
i 3 tmp_sum 10 tmp [3, 7] target 7
i 4 tmp_sum 3 tmp [3] target 7
i 2 tmp_sum 0 tmp [] target 7
i 2 tmp_sum 6 tmp [6] target 7
i 2 tmp_sum 12 tmp [6, 6] target 7
i 3 tmp_sum 6 tmp [6] target 7
i 3 tmp_sum 13 tmp [6, 7] target 7
i 4 tmp_sum 6 tmp [6] target 7
i 3 tmp_sum 0 tmp [] target 7
i 3 tmp_sum 7 tmp [7] target 7
i 3 tmp_sum 7
res [[2, 2, 3], [7]]
i 4 tmp_sum 0 tmp [] target 7
[[2, 2, 3], [7]]
'''
class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        n = len(candidates)
        res = []
        def backtrack(i, tmp_sum, tmp):
            print('backtrack的(i, tmp_sum, tmp)',i,tmp_sum,tmp)
            if  tmp_sum > target or i == n:
                return
            if tmp_sum == target:
                res.append(tmp)
                return
            for j in range(i, n):
                print('for j in range(i, n):的j',j)
                print('tmp_sum + candidates[j]',tmp_sum + candidates[j])
                if tmp_sum + candidates[j] > target:
                    break
                backtrack(j,tmp_sum + candidates[j],tmp+[candidates[j]])#j  在這裡
        backtrack(0, 0, [])
        return res
Solution().combinationSum([2,3,6,7],7)
"""
backtrack的(i, tmp_sum, tmp) 0 0 []
for j in range(i, n):的j 0
tmp_sum + candidates[j] 2
backtrack的(i, tmp_sum, tmp) 0 2 [2]
for j in range(i, n):的j 0
tmp_sum + candidates[j] 4
backtrack的(i, tmp_sum, tmp) 0 4 [2, 2]
for j in range(i, n):的j 0
tmp_sum + candidates[j] 6
backtrack的(i, tmp_sum, tmp) 0 6 [2, 2, 2]
for j in range(i, n):的j 0
tmp_sum + candidates[j] 8
for j in range(i, n):的j 1
tmp_sum + candidates[j] 7
backtrack的(i, tmp_sum, tmp) 1 7 [2, 2, 3]
for j in range(i, n):的j 2
tmp_sum + candidates[j] 10
for j in range(i, n):的j 1
tmp_sum + candidates[j] 5
backtrack的(i, tmp_sum, tmp) 1 5 [2, 3]
for j in range(i, n):的j 1
tmp_sum + candidates[j] 8
for j in range(i, n):的j 2
tmp_sum + candidates[j] 8
for j in range(i, n):的j 1
tmp_sum + candidates[j] 3
backtrack的(i, tmp_sum, tmp) 1 3 [3]
for j in range(i, n):的j 1
tmp_sum + candidates[j] 6
backtrack的(i, tmp_sum, tmp) 1 6 [3, 3]
for j in range(i, n):的j 1
tmp_sum + candidates[j] 9
for j in range(i, n):的j 2
tmp_sum + candidates[j] 9
for j in range(i, n):的j 2
tmp_sum + candidates[j] 6
backtrack的(i, tmp_sum, tmp) 2 6 [6]
for j in range(i, n):的j 2
tmp_sum + candidates[j] 12
for j in range(i, n):的j 3
tmp_sum + candidates[j] 7
backtrack的(i, tmp_sum, tmp) 3 7 [7]
"""