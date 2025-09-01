# You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.

# Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.

# Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.



from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev_height):
            # Check boundaries
            if (r < 0 or r >= rows or
                c < 0 or c >= cols):
                return

            # If this cell is already visited in current ocean's dfs, skip it
            if (r, c) in visited:
                return

            # If current cell's height < previous cell's height, water can't flow here
            if heights[r][c] < prev_height:
                return

            # Mark this cell as visited for current ocean
            visited.add((r, c))

            # Explore all four directions
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # Perform DFS from Pacific Ocean borders (top row and left column)
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])   # Top row
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])   # Left column

        # Perform DFS from Atlantic Ocean borders (bottom row and right column)
        for c in range(cols):
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])  # Bottom row
        for r in range(rows):
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])  # Right column

        # The result is the intersection of cells reachable from both oceans
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result
    
heights = [
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]

sol = Solution()
print(sol.pacificAtlantic(heights))
# Expected Output (order may vary):
# [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]