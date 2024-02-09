import re
from itertools import permutations

def operate(v1, v2, operator):
    if operator == '*':
        res = v1 * v2
    elif operator == '+':
        res = v1 + v2
    else:
        res = v1 - v2
    return res

def solution(expression):
    res = 0
    
    for priority in permutations('+-*'):
        operands = [int(x) for x in re.split('[+\-*]', expression)]
        operators = [x for x in expression if x in '+-*']
        
        for op in priority:
            while op in operators:
                i = operators.index(op)
                v = operate(operands[i], operands[i + 1], op)
                
                operands[i] = v
                operands.pop(i + 1)
                operators.pop(i)
        
        total = abs(operands.pop())
        res = max(total, res)
    
    return res