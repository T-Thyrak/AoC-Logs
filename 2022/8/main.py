from grid import parse_grid
import numpy as np

def main() -> None:
    grid = np.array(parse_grid("grid.txt"))
    
    mask = [[False for _ in range(grid.shape[1])] for _ in range(grid.shape[0])]
    highest_scenic_score = 0
    
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            trees_above = grid[:i, j]
            trees_below = grid[i + 1:, j]
            trees_left = grid[i, :j]
            trees_right = grid[i, j + 1:]
            
            if any(trees_above >= grid[i, j]) and any(trees_below >= grid[i, j]) and any(trees_left >= grid[i, j]) and any(trees_right >= grid[i, j]):
                mask[i][j] = True
                
            scenic_up = 0
            for k in range(i - 1, -1, -1):
                scenic_up += 1
                if grid[k, j] >= grid[i, j]:
                    break

            scenic_down = 0
            for k in range(i + 1, grid.shape[0]):
                scenic_down += 1
                if grid[k, j] >= grid[i, j]:
                    break
                
            scenic_left = 0
            for k in range(j - 1, -1, -1):
                scenic_left += 1 
                if grid[i, k] >= grid[i, j]:
                    break
            
            scenic_right = 0
            for k in range(j + 1, grid.shape[1]):
                scenic_right += 1
                if grid[i, k] >= grid[i, j]:
                    break
                
            scenic_score = scenic_up * scenic_down * scenic_left * scenic_right
            
            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score
                
    count = 99 * 99 - sum([sum(row) for row in mask])
    
    print(count)
    print(highest_scenic_score)
    pass


if __name__ == "__main__":
    main()