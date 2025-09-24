# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0 
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(right_depth, left_depth) + 1

# Build tree manually
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)

# Test
test = Solution()
print(test.maxDepth(root))   # Output: 3