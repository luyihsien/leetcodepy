trips = [[2,1,5],[3,3,7]]
trips=[[3,2,7],[3,7,9],[8,3,9]]
capacity =11
s=[]
e=[]
def takeSecond(elem):
    return elem[1]
trips.sort(key=takeSecond)
print(trips)
for i in trips:
    s.append(i[1])
    e.append(i[2])
print(s,e)
'''
class Solution:
    def carPooling(self, trips, capacity):
'''
trips=[[2,1,5],[3,3,7]]
capacity=4
for i in range(len(trips)):
    for j in trips[:i]:
        if j[2]<=trips[i][1]:
            capacity+=j[0]
            print(capacity)
    capacity-=trips[i][0]
    if capacity<0:
        if capacity < 0:
            print('False')
            break
    print('True')

class Solution:
    def carPooling(self, trips, capacity):
        def takeSecond(elem):
            return elem[1]
        trips.sort(key=takeSecond)
        print('trips',trips)
        for i in range(len(trips)):
            print('trips[:i]',trips[:i])
            for j in trips[:i]:
                print('j[2]',j[2])
                if j[2]<=trips[i][1]:
                    capacity+=j[0]
                    trips.remove(j)
                    print('capacity累加為',capacity)
            capacity-=trips[i][0]
            print('capcity減少為',capacity)
            if capacity<0:
                print('capacity negative',capacity)
                return False
        return True
#print(Solution().carPooling([[2,1,5],[3,3,7]],4))
print(Solution().carPooling([[8,2,3],[4,1,3],[1,3,6],[8,4,6],[4,4,8]],
12))




