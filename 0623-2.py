#第142場周賽
#Sirius 世界排名4
import collections
class Solution:
    def carPooling(self, trips, capacity):
        hashmap = collections.defaultdict(int)
        for n, s, e in trips:
            hashmap[s] += n
            hashmap[e] -= n
        cur = 0
        for i in sorted(hashmap):
            cur += hashmap[i]
            if cur > capacity:
                return False
        return True
#Arco 世界排名10
class Solution(object):
    def carPooling(self, trips, capacity):
        points = []
        for num, s, e in trips:#s:上車時間點 e:下車時間點
            points.append([s, 1, num])#拆成兩個List的項#較重要的放前面#同級時先下後上(故先加再減)
            points.append([e, 0, num])#用0 1判別加還是減 此處上車加下車減 算容量起伏比大小#要下必定以上過
            print(points)
        points.sort()
        print(points)
        cnt = 0
        for loc, st, num in points:
            print('cnt前',cnt)
            if st == 0:
                cnt -= num
                print('cnt減為',cnt)
            else:
                cnt += num
                print('cnt增為', cnt)
                if cnt > capacity:
                    return False
        return True
print(Solution().carPooling([[8,2,3],[4,1,3],[1,3,6],[8,4,6],[4,4,8]],
12))