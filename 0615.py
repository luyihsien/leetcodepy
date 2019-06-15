a=[[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
a.sort(reverse = True)
print(a)
count=0
b=a[0][0]
c=0
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = collections.defaultdict(list)
        for sid, score in items:
            scores[sid].append(score)
        ans = []
        i = 1
        for sid in sorted(scores):
            lst = scores[sid]
            ans.append([i, sum(heapq.nlargest(5, lst)) // 5])
            i += 1
        return ans





