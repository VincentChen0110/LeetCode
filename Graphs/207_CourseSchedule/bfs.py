# Explaination :
# https://leetcode.com/problems/course-schedule/discuss/368508/Python3-Breadth-first-search-for-cycle-detection
# Time Complexity O(V + E) Linear running time
from collections import deque, defaultdict
def canFinish(numCourses, prerequisites):
    todo = {i: set() for i in range(numCourses)} 
    graph = defaultdict(set)
    for i,j in prerequisites:
        todo[i].add(j)
        graph[j].add(i)
    q = deque([])
    for k,v in todo.items():
        if len(v) == 0:
            q.append(k)
    print(q)
    while q:
        n = q.popleft()
        print(n, "pop here")
        for i in graph[n]:
            todo[i].remove(n)
            if len(todo[i]) == 0:
                q.append(i)
        todo.pop(n)
    return not todo

numCourses = 6
prerequisites = [[2,1],[4,1],[3,2],[5,4],[2,3]]
print(canFinish(numCourses, prerequisites))