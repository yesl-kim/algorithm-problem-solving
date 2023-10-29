# 트리로 할 때
# 전체 시간복잡도는 find의 것으로 결정됨
class Union_Find_Tree:
    def __init__(self, N):
        self.root = list(range(N))
        self.height = [1]*N

    def find(self, x):
        # o(m), m은 집합 트리의 높이 (최악의 경우 n-1)
        # o(n)보다 작음
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        
        # 높이가 낮은 쪽 -> 높은 쪽으로 합침
        hx, hy = self.height[rx], self.height[ry]
        if hx < hy:
            self.root[rx] = ry
        else:
            self.root[ry] = rx
            
            if hx == hy:
                self.height[rx] += 1


# 배열로 할 때
# find - o(1)
# union - o(n)
class Union_Find_Arr:
    def __init__(self, size) -> None:
        self.root = list(range(size))
    
    def union(self, x, y):
        # y를 x에 합침
        # o(n)
        root_x, root_y = self.root[x], self.root[y] # find - o(1)
        for i, r in enumerate(self.root):
            if r == root_y:
                self.root[i] = root_x
