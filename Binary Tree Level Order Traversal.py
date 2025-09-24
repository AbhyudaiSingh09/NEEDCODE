# Definition for a binary tree node.
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root) ->int:
        if not root:
            return []
        result = []

        queue = deque([root])
        print("Current queue:", [node.val for node in queue])
        current_queue = [node.val for node in queue]
        while queue:
            level_size= len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result


# Build tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Run test
sol = Solution()
print(sol.levelOrder(root))   # Expected: [[3], [9, 20], [15, 7]]