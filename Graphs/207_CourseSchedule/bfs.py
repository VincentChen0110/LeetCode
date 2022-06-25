from collections import deque, defaultdict
def canFinish(numCourses, prerequisites):
    todo = {i: set() for i in range(numCourses)} 
    graph = defaultdict(set)
    for i,j in prerequisites:
        todo[i].add(j)
        graph[j].add(i)
    print(todo)
    print(graph)
    q = deque([])
    for k,v in todo.items():
        if len(v) == 0:
            q.append(k)
    while q:
        n = q.popleft()
        for i in graph[n]:
            todo[i].remove(n)
            if len(todo[i]) == 0:
                q.append(i)
        todo.pop(n)
    return not todo

numCourses = 2
prerequisites = [[1,0],[0,1]]
print(canFinish(numCourses, prerequisites))