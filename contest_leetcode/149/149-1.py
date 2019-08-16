#Space is O(N), time is still O(d ftarget)
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        state = [1] + [0 for i in range(target)]
        print('state',state)
        for i in range(d):
            for k in range(target, -1, -1):
                print('k',k)
                state[k] = 0
                print('min(f,k)',min(f,k))
                for j in range(1, min(f, k) + 1):
                    state[k] += state[k - j]
                    print('state',state)
        return state[-1] % (10 ** 9 + 7)
print(Solution().numRollsToTarget(d = 1, f = 6, target = 3))#1
print(Solution().numRollsToTarget(d = 2, f = 6, target = 7))
print(Solution().numRollsToTarget(d=6,f=6,target=36))

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}
        def dp(d, target):
            if d == 0:
                return 0 if target > 0 else 1
            if (d, target) in memo:
                return memo[(d, target)]
            to_return = 0
            for k in range(max(0, target-f), target):
                to_return += dp(d-1, k)
            memo[(d, target)] = to_return
            return to_return
        return dp(d, target) % (10**9 + 7)
print(Solution().numRollsToTarget(d = 2, f = 6, target = 6))

f=6
def dp(d, target):
    memo = {}
    if d == 0:
        return 0 if target > 0 else 1
    if (d, target) in memo:
        return memo[(d, target)]
    to_return = 0
    for k in range(max(0, target - f), target):
        to_return += dp(d - 1, k)
    memo[(d, target)] = to_return
    return to_return
print(dp(1,5))