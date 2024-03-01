from functools import reduce

def solution(m, musicinfos):
    notes = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a', 'B#': 'b'}
    def substitude_notes(s):
        converted = s
        for x, new in notes.items():
            converted = converted.replace(x, new)
        return converted
    
    def to_minutes(time):
        h, m = map(int, time.split(':'))
        return h * 60 + m

    def transform(info):
        start, end, title, music = info.split(',')
        music = substitude_notes(music)
        played_time = to_minutes(end) - to_minutes(start)

        cnt, rest = divmod(played_time, len(music))
        played = music * cnt + music[:rest]
        
        return played, title
    
    m = substitude_notes(m)
    def find(res, target):
        music = target[0]
        if m in music and len(music) > len(res[0]):
            return target
        return res
    
    res = reduce(find, map(transform, musicinfos), ('', '(None)'))
    return res[1]