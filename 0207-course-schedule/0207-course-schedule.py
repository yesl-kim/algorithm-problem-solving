from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prerequisites[i] = [a, b] => graph[b][a] (b -> a)
        graph = [[False] * numCourses for _ in range(numCourses)]
        degrees = [0] * numCourses
        
        for a, b in prerequisites:
            graph[b][a] = True
            degrees[a] += 1
        
        courses = deque()
        for i, d in enumerate(degrees):
            if d == 0:
                courses.append(i)
        
        while courses:
            c = courses.popleft()
            for next_course, degree in enumerate(graph[c]):
                if degree:
                    degrees[next_course] -= 1
                    if degrees[next_course] == 0:
                        courses.append(next_course)
        
        return all([d == 0 for d in degrees])
            