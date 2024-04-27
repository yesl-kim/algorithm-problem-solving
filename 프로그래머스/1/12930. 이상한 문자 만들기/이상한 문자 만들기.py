def solution(s):
    convert = lambda s: "".join(
        char.upper() if i % 2 == 0 else char.lower() 
        for i, char in enumerate(s)
    )
    
    return " ".join(convert(s) for s in s.split(" "))