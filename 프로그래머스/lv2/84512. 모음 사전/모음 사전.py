from itertools import permutations

def solution(word):
    words = []
    def combine(word): 
        if len(word) >= 5:
            return
        
        for char in 'AEIOU':
            w = word + char
            words.append(w)
            combine(w)
    
    combine('')
    words.sort()
    return words.index(word) + 1
        