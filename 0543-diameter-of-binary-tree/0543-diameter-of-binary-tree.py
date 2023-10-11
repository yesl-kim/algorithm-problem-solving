# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return -1
            
            return max(depth(node.left), depth(node.right)) + 1
        
        max_leng = 0
        def diameter(node):
            nonlocal max_leng
            if not node:
                return
            
            leng = depth(node.left) + depth(node.right) + 2
            max_leng = max(max_leng, leng)
            diameter(node.left)
            diameter(node.right)
        
        diameter(root)
        return max_leng
            