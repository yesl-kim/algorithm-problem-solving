def solution(s):
    nums = {
        'zero': '0',
        'one': '1',
        'two':'2',
        'three': '3',
        'four': '4',
        'five': '5', 
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    def find_prefix(s):
        for x in nums:
            if s.startswith(x):
                return x
        raise
           
    def parse(s):
        if not s:
            return ''
        
        char = s[0]
        if char.isdigit():
            return char + parse(s[1:])
        
        prefix = find_prefix(s)
        return nums[prefix] + parse(s[len(prefix):])
        
    return int(parse(s))
            
            
                