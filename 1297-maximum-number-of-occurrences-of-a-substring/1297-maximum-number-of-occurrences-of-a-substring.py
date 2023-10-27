from collections import defaultdict, Counter

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        subs_cnt = defaultdict(int)
        size = len(s)
        for i in range(size - minSize + 1):
            for e in range(i + minSize , min(i + maxSize + 1, len(s) + 1)):
                x = s[i:e]
                if len(Counter(x)) <= maxLetters:
                    subs_cnt[x] += 1
        return max(subs_cnt.values()) if subs_cnt else 0


# s = 'aababcaab'
# maxLetters = 2
# minSize = 3
# maxSize = 4
# print('=>', Solution().maxFreq(s, maxLetters, minSize, maxSize))