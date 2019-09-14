def dfs(g,v,q=[]):
    q.append(v)
    for i in g[v]:
        if i not in q:
            q=dfs(g,i,q)
    return q
g0={1:[2,3],2:[4,5],3:[5],4:[6],5:[6],6:[7],7:[]}
print(dfs(g0,1))