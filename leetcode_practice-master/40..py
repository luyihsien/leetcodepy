class Solution:
    def combinationSum2(self, candidates, target: int):
        if not candidates:
            return []
        candidates.sort()
        print('candidates',candidates)
        n = len(candidates)
        res = []

        def backtrack(i, tmp_sum, tmp_list):
            print('i',i,'tmp_sum',tmp_sum,'tmp_list',tmp_list)
            if tmp_sum == target:
                res.append(tmp_list)
                print('res',res)
                return
            for j in range(i, n):
                print('j',j)
                print('tmp_sum + candidates[j]',tmp_sum + candidates[j])
                if tmp_sum + candidates[j] > target: break
                print('i',i,'j',j)
                if j > i and candidates[j] == candidates[j - 1]: continue
                backtrack(j + 1, tmp_sum + candidates[j], tmp_list + [candidates[j]])

        backtrack(0, 0, [])
        return res
print(Solution().combinationSum2([2,5,2,1,2],5))