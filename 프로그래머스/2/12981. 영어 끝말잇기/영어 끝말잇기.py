def solution(n, words):
    befores = set()
    last_char = words[0][0]
    
    for i, word in enumerate(words):
        if last_char is not word[0] or word in befores:
            return [i % n + 1, i // n + 1]
        
        last_char = word[-1]
        befores.add(word)
    
    return [0, 0]
