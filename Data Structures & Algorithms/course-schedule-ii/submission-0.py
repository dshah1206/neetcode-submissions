class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjmap = {c:[] for c in range(numCourses)}

        for course, prereq in prerequisites:
            adjmap[course].append(prereq)

        result = []
        visited = set()
        cycle = set()
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)

            for pre in adjmap[course]:
                if not dfs(pre):
                    return False
            
            cycle.remove(course)
            visited.add(course)
            result.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return result


        