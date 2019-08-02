board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
#此處board[0][1]=B 第一格是y座標，第二格是x座標，誤弄反
class Solution:
    def exist(self, board: 'List[List[str]]', word: str) -> bool:

        row = len(board)#3
        col = len(board[0])#4
        def helper(i, j, k, visited):#i為y軸 j為x軸 k為str座標 visited為已訪的點
            print('helper({},{},{},{})'.format(i,j, k,visited))
            if k == len(word):#幹掉僅一個元素的類型
                return True
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:#回溯時只有 tmp_i 0 tmp_j 0是因之前已走訪過前三項#用意在於搞不好ABC的B上下都有C那退一步走另一個C看看，搞不好有機會
                tmp_i = x + i
                tmp_j = y + j
                print('tmp_i',tmp_i,'tmp_j',tmp_j)
                if 0 <= tmp_i < row and 0 <= tmp_j < col and (tmp_i, tmp_j) not in visited and board[tmp_i][tmp_j] == word[k]:#子遞迴沒東西無功而返，其父得到在if區得到None而入removed(平常再入遞迴或已return True)
                    #若不加上上面條件會因board對應不到值而error
                    visited.add((tmp_i, tmp_j))#紀錄已經訪問的點
                    print('visited',visited)
                    if helper(tmp_i, tmp_j, k + 1, visited):#遞迴#visited的順序沒差，靠的是參數去找(i,j)，visited只負責確認有無訪過
                        #print('helper({},{},{})'.format(i,j, k,visited))
                        return True
                    print('remove({},{})'.format(tmp_i,tmp_j))
                    visited.remove((tmp_i, tmp_j))
                    print('visited remove後的visted={}'.format(visited))# 回溯
            print('final visited',visited)#有add過才有本錢被remove
            return False



        for i in range(row):
            for j in range(col):
                print('board[{}][{}]={}'.format(i,j,board[i][j]),'word[0]={}'.format(word[0]))
                if board[i][j] == word[0] and helper(i, j, 1, {(i, j)}):#因字母可能不唯一故所有可能起點都是要試一次#1是刺探步，是1不是0
                    return True
        return False
print(Solution().exist(board,"ABCB"))
print(Solution().exist(board,"ABCESEEEFS"))
print(Solution().exist(board,"ABCESEECC"))
#a={(0,0)}
#a.add((0,1))
#print('a',a)#a {(0, 1), (0, 0)}
"""
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
"ABCCED"
false
预期结果
true
"""
#print(Solution().exist(board,"S"))
"""
输入:
[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
"ABCESEEEFS"
输出
false
预期结果
true
"""
#利用遞迴的順序性結合共用的sett去思考dfs的回溯對策