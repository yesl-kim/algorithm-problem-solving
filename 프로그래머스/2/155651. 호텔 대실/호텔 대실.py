import time
from heapq import heappush, heappop

def solution(book_time):
    def to_minutes(s):
        t = time.strptime(s, "%H:%M")
        return t.tm_hour * 60 + t.tm_min
        
    book_timestamps = [list(map(to_minutes, ts)) for ts in book_time]
    book_timestamps.sort(key=lambda x: (x[0], x[1]))
    
    rooms = []
    for start, end in book_timestamps:
        for i, last_time in enumerate(rooms):
            if last_time + 10 <= start:
                rooms[i] = end
                break
        else:
            rooms.append(end)
    return len(rooms)
                
        