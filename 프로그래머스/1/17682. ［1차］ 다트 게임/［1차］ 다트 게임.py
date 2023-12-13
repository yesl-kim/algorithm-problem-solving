def solution(dartResult):
    scores = []
    score_range = sorted((str(n) for n in range(11)), key=lambda s: len(s), reverse=True)
    quotients = {
        'S': 1,
        'D': 2,
        'T': 3
    }
    
    def get_prefix(s):
        for score in score_range:
            if s.startswith(score):
                return score
        return s[0]
    
    while dartResult:
        x = get_prefix(dartResult)
        if x.isdigit():
            scores.append(int(x))
        
        elif x == '*':
            scores[-1] *= 2
            if len(scores) > 1:
                scores[-2] *= 2
            
        elif x == '#':
            scores[-1] *= -1
        
        elif x in quotients:
            scores[-1] **= quotients[x]
        
        dartResult = dartResult[len(x):]

    return sum(scores)