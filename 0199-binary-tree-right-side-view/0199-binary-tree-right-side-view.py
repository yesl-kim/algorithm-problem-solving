# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        prev = (0, None)
        q = deque([(0, root)])
        while q:
            level, node = q.popleft()
            if node.left:
                q.append((level+1, node.left))
            if node.right:
                node.right and q.append((level+1, node.right))
            
            if prev[0] < level:
                res.append(prev[1].val)
            prev = (level, node)
        
        res.append(prev[1].val)
        return res