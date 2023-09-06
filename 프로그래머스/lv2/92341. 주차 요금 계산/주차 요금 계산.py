from collections import defaultdict
import datetime as dt
import math

def solution(fees, records):
    # 누적 주차시간 계산
    enters = {}
    parks = defaultdict(int)
    for r in records:
        time, car, type = r.split()
        h, m = map(int, time.split(':'))
        t = dt.timedelta(hours=h, minutes=m)
        
        if type == 'IN':
            enters[car] = t
        else:
            parks[car] += (t - enters[car]).seconds // 60
            del enters[car]
    
    if enters:
        for car, enter in enters.items():
            leave = dt.timedelta(hours=23, minutes=59)
            parks[car] += (leave - enter).seconds // 60
    
    # 주차요금 계산
    answer = []
    for car, time in sorted(parks.items()):
        over = time - fees[0]
        if over < 0:
            answer.append(fees[1])
        else:
            fee = fees[1] + math.ceil(over / fees[2]) * fees[3]
            answer.append(fee)
    
    return answer