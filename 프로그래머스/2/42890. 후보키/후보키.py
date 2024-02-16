from itertools import combinations

get_attribute_values = lambda col_indices, data: [tuple(data[row][col] for col in col_indices) for row in range(len(data))]

def is_subset(t1, t2):
    if len(t1) == len(t2):
        return t1 == t2
    
    super, sub = t1, t2
    if len(super) < len(sub):
        super, sub = sub, super

    return all(el in super for el in sub)

def solution(relation):
    col_size = len(relation[0])
    candidates = []
    
    for key_size in range(1, col_size + 1):
        for keys in combinations(range(col_size), key_size):
            values = get_attribute_values(keys, relation)
            if len(values) == len(set(values)) and not any(is_subset(keys, c) for c in candidates):
                candidates.append(keys)
    
    return len(candidates)