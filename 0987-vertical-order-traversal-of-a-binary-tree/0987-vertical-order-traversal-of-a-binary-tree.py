# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_map = defaultdict(list) # { col: List[TreeNode] }
        rows = {} # { TreeNode: row }
        
        q = deque()
        q.append((0, 0, root)) # (row, col, node)
        while q:
            row, col, node = q.popleft()
            if not node:
                continue
            
            col_map[col].append(node)
            rows[node] = row
            q.append((row + 1, col - 1, node.left))
            q.append((row + 1, col + 1, node.right))
            
        return [[node.val for node in 
                 sorted(col_map[c], key=lambda node: (rows[node], node.val))] 
                 for c in sorted(col_map)]