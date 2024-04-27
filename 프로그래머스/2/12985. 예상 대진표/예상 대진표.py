def group(arr, n):
    for i in range(0, len(arr), n):
        yield arr[i : i + n]

def solution(n, A, B):
    target_round = {A, B}
    
    def get_winner(a, b):
        if a in target_round and b in target_round:
            return None
        
        if a in target_round:
            return a
        
        if b in target_round:
            return b
        
        return a
        
    def run(matches, cnt):
        next_matches = []
        for a, b in group(matches, 2):
            winner = get_winner(a, b)
            if not winner:
                return cnt
            
            next_matches.append(winner)
        return run(next_matches, cnt + 1)
    
    return run(list(range(1, n + 1)), 1)
    
    