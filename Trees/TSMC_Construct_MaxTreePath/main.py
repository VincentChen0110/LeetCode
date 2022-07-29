from collections import defaultdict

fin_ans = 0

def dfs(i, visited, dic, values, ans):
    global fin_ans
    ans+=values[i]
    fin_ans = max(fin_ans,ans)
    visited[i]=True

    for j in range(len(dic[i])):
        if not visited[dic[i][j][0]]:
            dfs(dic[i][j][0], visited, dic, values, ans)

    visited[i] = False


def maxPathSum(parent,values):
    n = len(parent)
    dic = defaultdict(list)

    for i in range(n):
        if parent[i]!= -1:
            dic[parent[i]].append((i,values[i]))
            dic[i].append((parent[i],values[parent[i]]))
    
    for i in range(n):
        visited = [False] *n
        dfs(i, visited, dic,values, 0)
    return fin_ans

parent = [-1,0,0]
values = [5,-2,10]
print(maxPathSum(parent,values))