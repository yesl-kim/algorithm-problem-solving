from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = defaultdict(list)
        q = deque([(0, root)]) # (level, node)
        while q:
            level, node = q.popleft()
            if not node:
                continue
                
            nodes[level].append(node.val)
            q.append((level + 1, node.left))
            q.append((level + 1, node.right))
        
        return [nodes[level] for level in sorted(nodes)]