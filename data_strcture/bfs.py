#https://www.itread01.com/content/1542363063.html
#BFS、DFS和dijkstra演算法 -python
#有向圖
#https://www.itread01.com/content/1549793534.html
def bfs(graph, start):
    queue, visited = [start], [start]
    while queue:
        print('queue',queue)
        vertex = queue.pop()
        for i in graph[vertex]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    return visited
G={"A":{"B","D"},
    "B":{"C","E"},
    "C":{"E","F"},
    "D":{"G"},
    "E":{"D","F","G","H"},
    "F":{"H"},
    "G":{"H"},
    "H":{}}
print(bfs(G,'A'))