import math
from collections import Counter

def solution(str1, str2):
    get_elements = lambda s: [a + b for a, b in zip(s, s[1:]) if (a + b).isalpha()]
    total = lambda c: sum(c.values())
    
    c1 = Counter(get_elements(str1.lower()))
    c2 = Counter(get_elements(str2.lower()))
    
    union = total(c1 | c2)
    intersection = total(c1 & c2)
    print(union, intersection)
    similarity = intersection / union if union else 1
    return math.floor(similarity * 65536)