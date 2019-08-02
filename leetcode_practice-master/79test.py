board =[
  ['A','B','C','E'],
  ['S','C','C','S'],
  ['A','D','E','E']
]
class Solution:
    def exist(self, board: 'List[List[str]]', word: str) -> bool:

        row = len(board)#3
        col = len(board[0])#4
        def helper(i, j, k, visited):#i為y軸 j為x軸 k為str座標 visited為已訪的點
            print('helper({},{},{},{})'.format(i,j, k,visited))
            if k == len(word):#幹掉僅一個元素的類型
                return True
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:#先驗下上才驗左右#回溯時只有 tmp_i 0 tmp_j 0是因之前已走訪過前三項#用意在於搞不好ABC的B上下都有C那退一步走另一個C看看，搞不好有機會
                tmp_i = x + i
                tmp_j = y + j
                print('tmp_i',tmp_i,'tmp_j',tmp_j)
                if 0 <= tmp_i < row and 0 <= tmp_j < col and (tmp_i, tmp_j) not in visited and board[tmp_i][tmp_j] == word[k]:#子遞迴沒東西無功而返，其父得到在if區得到None而入removed(平常再入遞迴或已return True)
                    visited.add((tmp_i, tmp_j))#紀錄已經訪問的點
                    print('visited',visited)
                    if helper(tmp_i, tmp_j, k + 1, visited):#遞迴#visited的順序沒差，靠的是參數去找(i,j)，visited只負責確認有無訪過
                        #print('helper({},{},{})'.format(i,j, k,visited))
                        return True
                    print('remove({},{})'.format(tmp_i,tmp_j))
                    visited.remove((tmp_i, tmp_j))
                    print('visited remove後的visted={}'.format(visited))# 回溯
            return False



        for i in range(row):
            for j in range(col):
                print('board[{}][{}]={}'.format(i,j,board[i][j]),'word[0]={}'.format(word[0]))
                if board[i][j] == word[0] and helper(i, j, 1, {(i, j)}):#因字母可能不唯一故所有可能起點都是要試一次#1是刺探步，是1不是0
                    return True
        return False
print(Solution().exist(board,'ABCE'))