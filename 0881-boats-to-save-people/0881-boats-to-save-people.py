from collections import deque

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        cnt = 0
        people = deque(sorted(people))
        while people:
            x = people.pop()
            if people and people[0] + x <= limit:
                people.popleft()
            cnt += 1
        return cnt