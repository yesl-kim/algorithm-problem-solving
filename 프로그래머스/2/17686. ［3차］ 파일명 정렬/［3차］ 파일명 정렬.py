import re

def solution(files):
    pattern = re.compile('(\D+)(\d{1,5})(.*)')
    
    def sort_fn(s):
        head, number, tail = pattern.match(s).groups()
        return head.lower(), int(number)
    
    return sorted(files, key=sort_fn)
        