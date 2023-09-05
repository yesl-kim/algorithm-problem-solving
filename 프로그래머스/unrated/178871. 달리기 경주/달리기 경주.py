def solution(players, callings):
    index = {name: i for i, name in enumerate(players)}
    for cur in callings:
        i = index[cur]
        prev = players[i-1]

        players[i], players[i-1] = players[i-1], players[i]
        index[cur] -=1
        index[prev] += 1
    
    return sorted(index.keys(), key=lambda name: index[name])