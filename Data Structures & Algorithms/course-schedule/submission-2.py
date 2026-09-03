class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #If there is a cycle at any point, we are cooked

        visited = set()
        prereq = {} #Course --> prerequisites list

        for arr in prerequisites:
            if arr[0] in prereq:
                prereq[arr[0]].append(arr[1])
            else:
                prereq[arr[0]] = [arr[1]]

        #{0:3, 1:0, 2:1, 3:2, 4:0, 5:4}
        def dfs(course, path):
            
            if course in path:
                return False
            if course in visited:
                return True
            if course not in prereq: #Course has no prerequisites
                return True
            
            path.add(course)
            for pre in prereq[course]:
                if not dfs(pre, path):
                    return False
            
            path.remove(course)
            visited.add(course)
            return True

        for c in range(numCourses):
            if not dfs(c, set()):
                return False
        return True
