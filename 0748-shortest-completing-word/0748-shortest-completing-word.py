import re
from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        res = max(words, key=len) + 'xxx'
        origin = Counter(re.sub('[\d\s]', '', licensePlate).lower())
        
        for word in words:
            occurrences = Counter(word)
            if origin <= occurrences:
                res = min(res, word, key=len)
                
        return res