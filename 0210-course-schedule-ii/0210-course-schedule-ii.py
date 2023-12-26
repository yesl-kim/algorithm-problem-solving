class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        num_prerequisites = [0] * numCourses
        next_courses = defaultdict(list)
        for a, b in prerequisites:
            num_prerequisites[a] += 1
            next_courses[b].append(a)
            
        q = deque()
        for course, num in enumerate(num_prerequisites):
            if num == 0:
                q.append(course)

        res = []
        while q:
            c = q.popleft()
            res.append(c)
            for next_course in next_courses[c]:
                num_prerequisites[next_course] -= 1
                if num_prerequisites[next_course] == 0:
                    q.append(next_course)
        
        return res if len(res) == numCourses else []