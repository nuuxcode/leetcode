# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def mititi(node):
            if not node:
                return 0
            L= mititi(node.left)
            R= mititi(node.right)
            self.result=max(self.result,L+R)
            return max(L,R)+1
        dfs(root)
        return self.result
