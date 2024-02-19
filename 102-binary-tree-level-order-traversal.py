# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return

        result = []

        self.dfs(root, 0, result)
        return result

    def dfs(self, node, level, result):
        if not node:
            return

        if len(result) < level+1:
            result.append([])

        result[level].append(node.val)

        self.dfs(node.left, level+1, result)
        self.dfs(node.right, level+1, result)
