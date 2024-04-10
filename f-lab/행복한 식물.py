# o(mn)
# m = len(emotions)
# n = orders
def solution(initial_emotions, orders):
    emotions = list(initial_emotions)
    cnts = []
    for x in orders:
        for i, emotion in enumerate(emotions):
            if not emotion:
                continue
            emotions[i] = initial_emotions[i] if x == i + 1 else emotion - 1
        cnts.append(sum(e > 0 for e in emotions))
    return cnts
    


cases = (([2, 3, 1, 2], [3, 1, 2, 1, 4, 1], [4, 2, 2, 2, 2, 1]),
 ([5,5,5], [1, 2, 1, 2, 3],  [3, 3, 3, 3, 3]),
 ([5,5,5], [1, 2, 1, 2, 1],  [3, 3, 3, 3, 2]),
 ( [2, 1, 3, 4, 3], [2, 2, 2, 2, 5, 5, 5], [5, 4, 2, 1, 0, 0, 0]),
)

for i, (emotions, orders, expected) in enumerate(cases):
    output = solution(emotions, orders)
    print()
    print('-'*10)
    print(f"#case {i + 1}.", end=' ')
    if output == expected:
        print("✅")
        continue
    
    print("❌")
    print(f" emotions: {emotions}, orders: {orders}")
    print(f" expected: {expected}")
    print(f" output: {output}")
    print('-'*10)
    print()