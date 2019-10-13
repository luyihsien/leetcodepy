class Solution(object):
    def getMaximumGold(self, A):
        R, C = len(A), len(A[0])

        self.ans = 0

        def neighbors(r, c):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def search(r, c):
            for nr, nc in neighbors(r, c):
                if A[nr][nc]:
                    v = A[nr][nc]
                    A[nr][nc] = 0
                    self.bns += v
                    if self.bns > self.ans:
                        self.ans = self.bns
                    search(nr, nc)
                    A[nr][nc] = v
                    self.bns -= v

        for r in range(R):
            for c in range(C):
                if A[r][c]:
                    self.bns = v = A[r][c]
                    if self.bns > self.ans: self.ans = self.bns
                    A[r][c] = 0
                    search(r, c)
                    A[r][c] = v
        return self.ans