class Union_Find:
    def __init__(self, N):
        self.root = list(range(N))
        self.height = [1]*N

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def connect(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        
        hx, hy = self.height[rx], self.height[ry]
        if hx < hy:
            self.root[rx] = ry
        else:
            self.root[ry] = rx
            
            if hx == hy:
                self.height[rx] += 1

    def count(self, x):
        root = self.find(x)
        def count_children(parent):
            return sum(1 + count_children(c) for c, p in enumerate(self.root) if c != parent and p == parent)
        return count_children(root) + 1
    
    
def solution(n, wires):
    res = float('inf')
    for i in range(len(wires)):
        tree = Union_Find(n + 1) # 1 indexed, 1 ~ n
        new_wires = wires[:i] + wires[i+1:]
        for t1, t2 in new_wires:
            tree.connect(t1, t2)
        
        x, y = wires[i]
        res = min(res, abs(tree.count(x) - tree.count(y)))
    return res
    