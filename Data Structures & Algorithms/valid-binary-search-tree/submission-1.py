# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        return self.dfs(root, -math.inf, math.inf)
    def dfs(self, root, leftc, rightc):
        cond = leftc < root.val and root.val < rightc
        if root.left:
            cond = cond and self.dfs(root.left, leftc, min(rightc, root.val))
        if root.right:
            cond = cond and self.dfs(root.right, max(leftc, root.val), rightc)
        return cond
        