# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([(1, root)]) # depth, node
        max_depth = 0
        
        while q:
            depth, node = q.popleft()
            if not node:
                continue
            max_depth = max(max_depth, depth)
            q.append((depth + 1, node.left))
            q.append((depth + 1, node.right))
        
        return max_depth