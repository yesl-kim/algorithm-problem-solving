from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        indices = defaultdict(list)
        for i, char in enumerate(s):
            indices[char].append(i)

        uniques = [x for x in indices.values() if len(x) == 1]
        return uniques[0][0] if uniques else -1