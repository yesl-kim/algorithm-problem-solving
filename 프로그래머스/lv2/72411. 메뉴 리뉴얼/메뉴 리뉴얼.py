from itertools import combinations
from collections import Counter

def solution(orders, course):
    res = []
    
    for n in course:
        menus = []
        for order in orders:
            for menu in combinations(sorted(order), n):
                menus.append("".join(menu))
                
        if not menus:
            continue
        
        menu_cnts= Counter(menus).most_common()
        max_cnt = menu_cnts[0][1]
        res += (menu for menu, cnt in menu_cnts if cnt >= 2 and cnt == max_cnt)

    res.sort()
    return res