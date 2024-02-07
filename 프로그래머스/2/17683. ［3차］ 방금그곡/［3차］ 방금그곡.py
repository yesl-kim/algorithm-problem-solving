
def solution(m, musicinfos):    
    notes = {'C#': 'c', 'D#': 'd', "F#": 'f', "G#": 'g', 'A#': 'a'}
    
    def parse_music(m):
        parsed = m
        for note, s in notes.items():
            parsed = parsed.replace(note, s)
        return parsed

    def to_minutes(time):
        hour, minuite = map(int, time.split(':'))
        return hour * 60 + minuite
    
    musics = []
    melody = parse_music(m)
    for info in musicinfos:
        start, end, title, music = info.split(',')
        duration = to_minutes(end) - to_minutes(start)

        parsed_music = parse_music(music)
        몫, 나머지 = divmod(duration, len(parsed_music))
        played = parsed_music * 몫 + parsed_music[:나머지]

        if melody in played:
            musics.append((played, title))
    
    musics.sort(key=lambda x: len(x[0]), reverse=True)
    return musics[0][1] if musics else "(None)"