'''
d={'1':'s','2':{'t','e'}}
for i in d['2']:
    print(i)
print(type({'t','e'}))

def bfs(g,s):
    q,v=[s],[s]
    while q:
        ve=q.pop(0)
        print('ve',ve)
        for i in g[ve]:
            if i not in v:
                v.append(i)
                q.append(i)
        print('v', v)
        print('q',q)
    return v
G={'A':{'B','D'},
   'B':{'C','E'},
   'C':{'E','F'},
   'D':{'G'},
   'E':{"D","F","G","H"},
   'F':{'H'},
   'G':{'H'},
   'H':{}
   }
print(bfs(G,'A'))
'''
def bfs(g,s):
    q,v=[s],[s]
    while q:
        ve=q.pop(0)
        print('ve',ve)
        for i in g[ve]:
            if i not in v:
                v.append(i)
                q.append(i)
        print('v', v)
        print('q',q)
    return v
G={'A':['B','D'],
   'B':['C','E'],
   'C':['E','F'],
   'D':['G'],
   'E':["D","F","G","H"],
   'F':['H'],
   'G':['H'],
   'H':[]
   }
print(bfs(G,'A'))
c=['B','A']
c.sort()
print(c)#['A', 'B']
#故可以
#for i in G:
    #G[i].sort()
