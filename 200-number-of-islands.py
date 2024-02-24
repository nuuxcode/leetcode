class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            try:
                rows= len(grid)
                cols= len(grid[0])
                if row < 0 or col < 0 or grid[row][col] == "0":
                    return
                grid[row][col] = "0"
                dfs(row,col-1)
                dfs(row-1,col)
                dfs(row+1,col)
                dfs(row,col+1)
            except:
                return

        counter = 0
        rows= len(grid)
        cols= len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    counter +=1
                    dfs(row, col)
        return counter
