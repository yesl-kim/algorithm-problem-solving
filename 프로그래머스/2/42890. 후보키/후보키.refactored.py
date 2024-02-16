from itertools import combinations

get_attribute_values = lambda col_indices, data: [tuple(item[i] for i in col_indices) for item in data]

def is_subset(t1, t2):
    if len(t1) == len(t2):
        return t1 == t2
    
    super, sub = t1, t2
    if len(super) < len(sub):
        super, sub = sub, super

    return all(el in super for el in sub)

def solution(relation):
    data_size = len(relation)
    col_size = len(relation[0])
    candidates = []
    
    for key_size in range(1, col_size + 1):
        for keys in combinations(range(col_size), key_size):
            values = get_attribute_values(keys, relation)
            if len(set(values)) == data_size and not any(is_subset(keys, c) for c in candidates):
                candidates.append(keys)
    
    return len(candidates)