class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prereq_map = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if prereq_map[course] == []:
                return True

            visited.add(course)

            for pre in prereq_map[course]:
                if not dfs(pre):
                    return False

            visited.remove(course)
            prereq_map[course] = []

            return True
            
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True