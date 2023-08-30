from collections import defaultdict

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = defaultdict(list)
        
        for i, x in enumerate(list1):
            for j, y in enumerate(list2):
                if x == y:
                    common[i+j].append(x)
        
        return common[sorted(common)[0]]