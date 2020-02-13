def numIslands(self, grid: List[List[str]]) -> int:
        def traverse(grid, i, j):
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == '0':
                return 
            grid[i][j] = '0'
            traverse(grid, i, j+1)
            traverse(grid, i, j-1)
            traverse(grid, i+1, j)
            traverse(grid, i-1, j)
        numOfIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    numOfIslands += 1
                    traverse(grid, i, j)
        return numOfIslands