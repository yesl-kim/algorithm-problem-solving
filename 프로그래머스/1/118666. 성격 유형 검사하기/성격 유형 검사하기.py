def solution(survey, choices):
    types = ["".join(sorted(t)) for t in ['RT', 'CF', 'JM', 'AN']]
    scores = {t: 0 for t in types}
    
    mid = round(7 / 2)
    for i, x in enumerate(choices):
        t = survey[i]
        if t in types:
            scores[t] += x - mid
        else:
            t = "".join(sorted(t))
            scores[t] -= x - mid
    
    personal_type = [t[0] if score <= 0 else t[1] for t, score in scores.items()]
    return "".join(personal_type)