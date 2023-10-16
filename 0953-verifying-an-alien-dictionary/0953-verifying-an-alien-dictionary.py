class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {char: i for i, char in enumerate(order)}
        
        for ws in zip(words, words[1:]):
            for c1, c2 in zip(*ws):
                a, b = order[c1], order[c2]
                if a < b:
                    break
                elif a > b:
                    return False
            else:
                if len(ws[0]) > len(ws[1]):
                    return False
        
        return True