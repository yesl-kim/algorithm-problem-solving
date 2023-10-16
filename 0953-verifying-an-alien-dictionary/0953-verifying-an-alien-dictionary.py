class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {char: i+1 for i, char in enumerate(order)}
        order['_'] = 0
        
        max_len = max(map(len, words))
        words = [w.ljust(max_len, '_') for w in words]
        for ws in zip(words, words[1:]):
            for c1, c2 in zip(*ws):
                a, b = order[c1], order[c2]
                if a < b:
                    break
                elif a > b:
                    return False
        
        return True