import re

def solution(files):
    def sort_fn(s):
        pattern = re.compile('(\D+)(\d{1,5})(.*)')
        matched = pattern.match(s)
        if matched:
            head, number, tail = matched.groups()
            return (head.lower(), int(number))
    
    return sorted(files, key=sort_fn)
        