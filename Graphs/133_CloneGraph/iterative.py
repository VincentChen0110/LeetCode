## BFS Solution
# To solve this problem we need two things:

# BFS to traverse the graph
# A hash map to keep track of already visited and already cloned nodes
# We push a node in the queue and make sure that the node is already cloned. Then we process neighbors. If a neighbor is already cloned and visited, we just append it to the current clone neighbors list, otherwise, we clone it first and append it to the queue to make sure that we can visit it in the next tick.

# Time: O(V + E) - for BFS
# Space: O(V) - for the hashmap

# Runtime: 32 ms, faster than 98.18% of Python3 online submissions for Clone Graph.
# Memory Usage: 14.4 MB, less than 91.72% of Python3 online submissions for Clone Graph.
def cloneGraph(self, node: 'Node') -> 'Node':
    if not node: return node
    
    q, clones = deque([node]), {node.val: Node(node.val, [])}
    while q:
        cur = q.popleft() 
        cur_clone = clones[cur.val]            

        for ngbr in cur.neighbors:
            if ngbr.val not in clones:
                clones[ngbr.val] = Node(ngbr.val, [])
                q.append(ngbr)
                
            cur_clone.neighbors.append(clones[ngbr.val])
            
    return clones[node.val]