def solution(m, musicinfos):
    notes = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a', 'B#': 'b'}
    def convert_music(s):
        converted = s
        for x, new in notes.items():
            converted = converted.replace(x, new)
        return converted
    
    def get_duration(time):
        h, m = map(int, time.split(':'))
        return h * 60 + m
    
    def is_matched(musicinfo):
        start, end, title, music = x.split(',')
        music = converted(music)
        
        played_time = get_duration(end) - get_duration(start)
        c, rest = divmod(played_time, len(music))
        
        played = music * c + music[:rest]
        return m in played
    
    m = convert_music(m)
    listened = []
    for x in musicinfos:
        start, end, title, music = x.split(',')
        music = convert_music(music)
        
        played_time = get_duration(end) - get_duration(start)
        c, rest = divmod(played_time, len(music))
        
        played = music * c + music[:rest]
        if m in played:
            listened.append((played, title))
    
    listened.sort(key=lambda x: len(x[0]), reverse=True)
    return listened[0][1] if listened else '(None)'
    
        