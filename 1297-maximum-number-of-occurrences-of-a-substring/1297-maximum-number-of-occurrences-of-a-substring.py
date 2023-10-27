from collections import defaultdict, Counter

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        subs_cnt = defaultdict(int)
        
        for i in range(len(s)):
            for size in range(minSize, maxSize + 1):
                if len(s) < i + size:
                    break
                x = s[i: i + size]
                if len(set(x)) <= maxLetters:
                    subs_cnt[x] += 1
        
        return max(subs_cnt.values()) if subs_cnt else 0


# s = 'aababcaab'
# maxLetters = 2
# minSize = 3
# maxSize = 4
# print('=>', Solution().maxFreq(s, maxLetters, minSize, maxSize))