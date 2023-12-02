from typing import List

def minMeetingRooms(times: List[int]):
    times.sort(key=lambda x: (x[0], x[1]))
    
    rooms = []
    for start, end in times:
        for i, last_time in enumerate(rooms):
            if last_time <= start:
                rooms[i] = end
                break
        else:
            rooms.append(end)
    
    return len(rooms)

print(minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
print(minMeetingRooms( [[7, 10], [2, 4]]))
print(minMeetingRooms([[3, 6], [6, 10], [10, 12], [12, 15], [15, 30]]))
