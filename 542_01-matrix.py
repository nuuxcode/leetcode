class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        queue = deque()
        rows = len(mat)
        cols = len(mat[0])
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r,c))
                else:
                    mat[r][c] = float('inf')

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            r,c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r+dr , c+dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if mat[nr][nc] > mat[r][c] + 1:
                        mat[nr][nc] = mat[r][c] + 1
                        queue.append((nr, nc))
        return mat
