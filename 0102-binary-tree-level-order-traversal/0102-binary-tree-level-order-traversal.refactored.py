from itertools import zip_longest

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, node: Optional[TreeNode]) -> List[List[int]]:
        if not node:
            return []
        left = self.levelOrder(node.left)
        right = self.levelOrder(node.right)
        return [[node.val]] + [l + r for l, r in zip_longest(left, right, fillvalue=[])]