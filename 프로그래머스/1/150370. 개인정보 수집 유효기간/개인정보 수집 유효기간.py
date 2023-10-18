from datetime import datetime, date
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    today = datetime.strptime(today, "%Y.%m.%d")
    validities = {}
    for term in terms:
        t, v = term.split()
        validities[t] = int(v)
        
    for i, p in enumerate(privacies):
        d, t = p.split()
        after = relativedelta(months=validities[t])
        
        if datetime.strptime(d, "%Y.%m.%d") + after <= today:
            answer.append(i+1)
        
    return answer