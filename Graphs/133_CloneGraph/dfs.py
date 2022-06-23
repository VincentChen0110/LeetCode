class Solution(object):
    # time complexity is O(E)
    # Space complexity is O(E+V) = O(E) for connected graph
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        mp = {}
        if not node: return node
        def dfs(cur):
            clone = Node(val = cur.val)
            mp[cur] = clone
            for ns in cur.neighbors:
                if ns not in mp: dfs(ns)
                clone.neighbors.append(mp[ns])
            return clone
        return dfs(node)