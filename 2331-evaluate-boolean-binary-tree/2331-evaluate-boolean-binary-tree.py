# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_leaf(self, node):
        return node.val == 0 or node.val == 1
    
    def operator(self, node):
        return any if node.val == 2 else all
    
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if self.is_leaf(root):
            return bool(root.val)
        
        return self.operator(root)(map(self.evaluateTree, (root.left, root.right)))