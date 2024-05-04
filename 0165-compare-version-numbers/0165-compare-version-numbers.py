from itertools import zip_longest

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for pair in zip_longest(version1.split('.'), version2.split('.'), fillvalue='0'):
            a, b = map(int, pair)
            if a < b:
                return -1
            elif a > b:
                return 1
        return 0