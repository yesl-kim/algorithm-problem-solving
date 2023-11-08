# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def _max_depth(node, depth = 0):
            if not node:
                return depth
            return max(_max_depth(node.left, depth + 1), _max_depth(node.right, depth + 1))
        return _max_depth(root)