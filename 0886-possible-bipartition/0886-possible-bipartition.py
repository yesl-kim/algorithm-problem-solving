class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dislikes_map = defaultdict(set)
        for a, b in dislikes:
            dislikes_map[a].add(b)
            dislikes_map[b].add(a)
        
        group = defaultdict(int) # -1, 0, 1
        def can_put_person(person, i):
            g = group[person]
            if not g:
                group[person] = i
                return all(can_put_person(dislike, -i) for dislike in dislikes_map[person])
            return g == i
        
        for person in range(1, n + 1):
            if not group[person]:
                if not can_put_person(person, 1):
                    return False
        return True