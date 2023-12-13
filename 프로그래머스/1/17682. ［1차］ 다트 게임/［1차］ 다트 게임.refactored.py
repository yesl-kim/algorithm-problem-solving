import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    options = {'' : 1, '*' : 2, '#' : -1}
    pattern = re.compile('(\d+)([SDT])([*#]?)')
    dart = pattern.findall(dartResult)
    scores = [0]
    for i, (score, area, option) in enumerate(dart):
        if option == '*':
            scores[i] *= 2
        scores.append(int(score) ** bonus[area] * options[option])

    return sum(scores)