from collections import defaultdict, Counter

key = lambda s: str(hash(''.join(sorted(s))))

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for s in strs:
            anagrams[key(s)].append(s)
                
        return anagrams.values()