from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prerequisites[i] = [a, b] => graph[b][a] (b -> a)
        graph = [[] for _ in range(numCourses)]
        degrees = [0] * numCourses
        
        for a, b in prerequisites:
            graph[b].append(a)
            degrees[a] += 1
        
        courses = deque()
        for i, d in enumerate(degrees):
            if d == 0:
                courses.append(i)
        
        cnt = 0
        while courses:
            c = courses.popleft()
            cnt += 1
            
            for next_course in graph[c]:
                degrees[next_course] -= 1
                if degrees[next_course] == 0:
                    courses.append(next_course)
        
        return cnt == numCourses
            