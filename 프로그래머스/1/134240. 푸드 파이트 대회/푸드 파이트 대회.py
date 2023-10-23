def solution(food):
    answer = '0'
    for i in range(len(food)-1, 0, -1):
        x = str(i) * (food[i] // 2)
        answer = x + answer + x
        
    return answer