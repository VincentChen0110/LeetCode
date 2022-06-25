def canFinish(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    graph = [[] for _ in range(numCourses)]
    visited = [0 for _ in range(numCourses)]
    
    def dfs(graph, visited, i):
        # if visited, cycle found
        if visited[i] == -1: return False
        if visited[i] == 1: return True
        visited[i] = -1
        for c in graph[i]:
            if not(dfs(graph,visited,c)):
                return False
        visited[i] = 1
        return True
    
    for x, y in prerequisites:
        graph[x].append(y)
    
    for i in range(numCourses):
        if not(dfs(graph,visited,i)):
            return False
    return True