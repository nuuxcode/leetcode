"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        from collections import deque
        if not node:
            return node
        visited = { node : Node(node.val)}
        queue = deque([node])
        while queue:
            nodex = queue.popleft()
            for neighbor in nodex.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[nodex].neighbors.append(visited[neighbor])
        return visited[node]
